package com.example.quizgame

data class Question(
    val text: String?,
    val action: String?,
    val involvedPlayers: List<Int>?
)
