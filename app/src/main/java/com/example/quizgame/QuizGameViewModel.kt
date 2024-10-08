package com.example.quizgame

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel

class QuizGameViewModel : ViewModel() {
    private val gameRepository = GameRepository()
    var playerCount by mutableStateOf(2)
    var playerNames by mutableStateOf(List(2) { "" })
    var currentQuestionIndex by mutableStateOf(0)
    var gameState by mutableStateOf(GameState.SETUP)
    var questions by mutableStateOf(emptyList<Question>())

    fun updatePlayerCount(count: Int) {
        playerCount = count.coerceIn(2, 10)
        playerNames = List(playerCount) { index -> playerNames.getOrElse(index) { "" } }
    }

    fun updatePlayerName(index: Int, name: String) {
        playerNames = playerNames.toMutableList().apply { set(index, name) }
    }

    fun startGame() {
        questions = gameRepository.getQuestions().shuffled()
        gameState = GameState.PLAYING
        currentQuestionIndex = 0
    }

    fun nextQuestion() {
        if (currentQuestionIndex < questions.lastIndex) currentQuestionIndex++
        else gameState = GameState.FINISHED
    }

    fun resetGame() {
        gameState = GameState.SETUP
        currentQuestionIndex = 0
    }

    fun getCurrentQuestionText(): String {
        val question = questions[currentQuestionIndex]
        return when {
            question.text != null -> question.text
            question.action != null -> {
                val involvedPlayerNames = question.involvedPlayers?.mapNotNull { playerNames.getOrNull(it) } ?: emptyList()
                String.format(question.action, *involvedPlayerNames.toTypedArray())
            }
            else -> ""
        }
    }
}

enum class GameState { SETUP, PLAYING, FINISHED }
