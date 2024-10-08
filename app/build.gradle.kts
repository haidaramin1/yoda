plugins {
    id("com.android.application")
    kotlin("android")
    id("org.jetbrains.kotlin.plugin.compose") version "2.0.0" // Använd den senaste stabila versionen
}

android {
    compileSdk = 34 // Update as per your target SDK

    defaultConfig {
        applicationId = "com.example.quizgame"
        minSdk = 24
        targetSdk = 34
        versionCode = 1
        versionName = "1.0"
    }

    namespace = "com.example.quizgame"

    buildFeatures {
        compose = true
    }

    composeOptions {
        kotlinCompilerExtensionVersion = "2.0.0" // Ensure this matches your Compose version
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }

    kotlinOptions {
        jvmTarget = "1.8"
    }
}

dependencies {
    implementation("androidx.compose.ui:ui:1.7.3") // UI elements
    implementation("androidx.compose.material:material:1.7.3") // Material Design components
    implementation("androidx.compose.material3:material3:1.3.0") // Material3 components (if needed)
    implementation("androidx.navigation:navigation-compose:2.8.2") // Navigation component
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.8.6") // Lifecycle view model
    debugImplementation("androidx.compose.ui:ui-tooling:1.7.3") // UI tooling for debugging
    implementation("androidx.compose.compiler:compiler:1.5.15") // Compose compiler
}
