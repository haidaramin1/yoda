package com.example.quizgame

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import com.example.quizgame.ui.theme.QuizGameTheme

class MainActivity : ComponentActivity() {
    private val viewModel: QuizGameViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            QuizGameTheme {
                QuizGameApp(viewModel)
            }
        }
    }
}
