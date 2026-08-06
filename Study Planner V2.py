import os
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

try:
    import openai
except ImportError:
    openai = None  # type: ignore[assignment]

class DuolingoStyleTutor:
    def __init__(self, raw_study_material):
        self.raw_material = raw_study_material
        self.curriculum = []
        self.current_step = 0
        self.hearts = 3
        self.xp = 0
        self.client = None

    def _get_client(self):
        if openai is None:
            raise ImportError("The 'openai' package is required. Install it with 'pip install openai'.")

        if self.client is None:
            api_key = os.environ.get("OPENAI_API_KEY")
            if hasattr(openai, "OpenAI"):
                self.client = openai.OpenAI(api_key=api_key)
            else:
                if api_key:
                    openai.api_key = api_key
                self.client = openai

        return self.client

    def _create_chat_completion(self, model, messages, temperature=None, response_format=None):
        client = self._get_client()
        kwargs = {"model": model, "messages": messages}
        if temperature is not None:
            kwargs["temperature"] = temperature
        if response_format is not None and hasattr(client, "chat"):
            kwargs["response_format"] = response_format

        if hasattr(client, "chat") and hasattr(client.chat, "completions"):
            return client.chat.completions.create(**kwargs)

        if hasattr(client, "ChatCompletion") and hasattr(client.ChatCompletion, "create"):
            return client.ChatCompletion.create(**kwargs)

        raise RuntimeError(
            "Unsupported OpenAI client API. Install a compatible openai version with 'pip install --upgrade openai'."
        )

    def _extract_response_text(self, response):
        if hasattr(response, "choices"):
            choices = getattr(response, "choices")
            if isinstance(choices, (list, tuple)) and choices:
                choice = choices[0]
                if hasattr(choice, "message") and hasattr(choice.message, "content"):
                    return choice.message.content
            if hasattr(choices, "message") and hasattr(choices.message, "content"):
                return choices.message.content

        try:
            return response["choices"][0]["message"]["content"]
        except Exception:
            pass

        raise ValueError("Unable to extract message content from the OpenAI response.")

    def generate_curriculum(self):
        """
        THE ARCHITECT: Uses GPT to transform raw text into a strict,
        linear, gamified JSON curriculum structure.
        """
        print("🧠 Processing your study material into micro-lessons... Please wait.")
        
        prompt = f"""
        You are the 'Curriculum Architect' for a Duolingo-style micro-learning app.
        Take the following raw study material and break it down into a linear sequence of exactly 3 micro-concepts.
        For each micro-concept, generate a tiny explanation, a multiple choice question, the correct answer, and 3 incorrect options.
        
        Raw Material: {self.raw_material}
        
        You MUST return your response as a strict JSON array matching this exact format, with no markdown code blocks or wrapper text:
        [
          {{
            "concept_name": "Name of micro-concept",
            "micro_explanation": "1-2 sentences maximum introducing the concept clearly.",
            "question": "A punchy multiple-choice question testing the explanation.",
            "correct_answer": "The right answer string",
            "wrong_answers": ["Wrong choice 1", "Wrong choice 2", "Wrong choice 3"]
          }}
        ]
        """

        response = self._create_chat_completion(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"} if hasattr(self._get_client(), "chat") else None,
        )

        raw_data = json.loads(self._extract_response_text(response))
        self.curriculum = raw_data if isinstance(raw_data, list) else list(raw_data.values())[0]
        print("✅ Curriculum built! Let's start learning.\n")

    def get_hype_feedback(self, concept_name):
        """
        THE HYPE MAN: Generates an explosive, positive sentence of 
        encouragement to keep the user motivated.
        """
        prompt = f"Give a one-sentence burst of high-energy, enthusiastic praise to a student who just mastered the concept: '{concept_name}'. Include 1-2 celebratory emojis. Keep it short!"
        response = self._create_chat_completion(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9,
        )
        return self._extract_response_text(response)

    def play_game(self):
        """
        THE STATE MACHINE GAME LOOP: Executes the rigid step-by-step 
        Duolingo game rules in the terminal.
        """
        if not self.curriculum:
            print("⚠️ No curriculum generated. Please process material first.")
            return

        while self.current_step < len(self.curriculum) and self.hearts > 0:
            lesson = self.curriculum[self.current_step]
            
            print(f"==================================================")
            print(f"🌟 LESSON {self.current_step + 1}/{len(self.curriculum)}: {lesson['concept_name']}")
            print(f"❤️ Hearts: {self.hearts} | ✨ XP: {self.xp}")
            print(f"==================================================")
            
            # 1. Micro-learning phase
            print(f"\n📖 Learn this:\n{lesson['micro_explanation']}\n")
            input("Press Enter when you're ready for the micro-quiz... 🏃‍♂️")
            
            # 2. Build the quiz options
            import random
            options = [lesson['correct_answer']] + lesson['wrong_answers']
            random.shuffle(options)
            
            print(f"\n❓ Question:\n{lesson['question']}")
            for idx, opt in enumerate(options):
                print(f"  {idx + 1}. {opt}")
                
            # 3. Handle user answer input safely
            try:
                user_choice = int(input("\nChoose the correct option (1-4): ")) - 1
                selected_answer = options[user_choice]
            except (ValueError, IndexError):
                print("\n❌ Invalid input! That costs you a heart for not paying attention!")
                self.hearts -= 1
                continue

            # 4. Check answer against state rules
            if selected_answer == lesson['correct_answer']:
                self.xp += 10
                self.current_step += 1
                hype = self.get_hype_feedback(lesson['concept_name'])
                print(f"\n🎉 CORRECT! {hype}\n")
            else:
                self.hearts -= 1
                print(f"\n❌ INCORRECT! The correct answer was: {lesson['correct_answer']}")
                print("Don't worry, mistakes help you learn! Let's try a different concept layout.\n")
                
        # 5. Game over screen
        if self.hearts <= 0:
            print("💀 GAME OVER! You ran out of hearts. Let's rest your brain and try again later!")
        else:
            print(f"🏆 CONGRATULATIONS! You completed the course! Final XP: {self.xp} ✨")

# ==========================================
# RUNNING THE APP ENGINES WITH SAMPLE DATA
# ==========================================
if __name__ == "__main__":
    # Simulate a user pasting notes from a Biology lecture
    sample_pdf_notes = """
    Photosynthesis is the process used by plants to convert light energy into chemical energy. 
    It mostly happens in the leaves, inside tiny structures called chloroplasts. Chloroplasts contain 
    chlorophyll, a green pigment that absorbs the sunlight. During the process, plants take in Carbon Dioxide (CO2) 
    from the air and Water (H2O) from the soil. They use the sun's energy to turn these into Glucose (sugar), 
    which is their food, and they release Oxygen (O2) back into the air as a waste product.
    """
    
    # Initialize our system, build the map, and start the interactive game loop
    tutor_app = DuolingoStyleTutor(sample_pdf_notes)
    tutor_app.generate_curriculum()
    tutor_app.play_game()