package com.example.quizgame

class GameRepository {
    fun getQuestions(): List<Question> {
        // Replace with your actual data fetching logic
        return listOf(
            Question("What is the capital of France?", null, null),
            Question(null, "Take a sip", listOf(0, 1)),
            // Add more questions as needed
        )
    }
}
