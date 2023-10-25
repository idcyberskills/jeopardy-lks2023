package com.siahaan.bagpack.utils

import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.ktx.storage
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.tasks.await
import kotlinx.coroutines.withContext
import java.io.File

class FirebaseStorageManager {

    private val storage = Firebase.storage("gs://bagpack---lksn2023.appspot.com")

    suspend fun downloadEncryptedFile(filePath: String): File? {
        return withContext(Dispatchers.IO) {
            try {
                val storageRef = storage.reference.child(filePath)
                val localFile = File.createTempFile("data_", ".enc")
                storageRef.getFile(localFile).await()

//                println("Data Path: ${localFile.absolutePath}")

                localFile.deleteOnExit()
                localFile
            } catch (e: Exception) {
                // Handle exceptions (e.g., file not found, network error)
                e.printStackTrace()
                null
            }
        }
    }
}