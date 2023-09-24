import random


class FitnessAssistant:
    def __init__(self):
        self.profile = self.create_user_profile()
        self.recommendations = self.get_fitness_recommendations()

    def create_user_profile(self):
        return {
            "name": "John Doe",
            "age": 30,
            "weight": 75,
            "height": 180,
            "activity_level": "Moderate",
            "fitness_goals": ["Weight loss", "Muscle gain"],
        }

    def get_fitness_recommendations(self):
        return {
            "workout_routine": self.generate_workout_routine(),
            "nutrition_plan": self.generate_nutrition_plan(),
            "exercise_techniques": self.generate_exercise_techniques(),
        }

    def generate_workout_routine(self):
        return {
            "Monday": "Cardio",
            "Tuesday": "Strength training",
            "Wednesday": "Rest",
            "Thursday": "Cardio",
            "Friday": "Strength training",
            "Saturday": "Rest",
            "Sunday": "Active recovery",
        }

    def generate_nutrition_plan(self):
        return {
            "calorie_intake": 2000,
            "macronutrients": {"protein": 120, "carbs": 200, "fat": 60},
        }

    def generate_exercise_techniques(self):
        techniques = ["Squats", "Push-ups", "Plank"]
        return random.sample(techniques, k=3)

    def interact_with_user(self):
        print("Hello! I am your personal fitness assistant.")
        print(f"Let's get started with your fitness journey, {self.profile['name']}!")
        print("Here are some fitness recommendations for you:")

        print("Workout Routine:")
        for day, workout in self.recommendations["workout_routine"].items():
            print(f"{day}: {workout}")

        print("\nNutrition Plan:")
        print(
            f"Calorie Intake: {self.recommendations['nutrition_plan']['calorie_intake']} calories"
        )
        print("Macronutrients:")
        for nutrient, value in self.recommendations["nutrition_plan"][
            "macronutrients"
        ].items():
            print(f"{nutrient.capitalize()}: {value} grams")

        print("\nExercise Techniques:")
        for technique in self.recommendations["exercise_techniques"]:
            print(f"- {technique}")

        print("\nFeel free to ask me any fitness-related questions!")


if __name__ == "__main__":
    assistant = FitnessAssistant()
    assistant.interact_with_user()
