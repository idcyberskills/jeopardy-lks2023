package com.siahaan.bagpack.utils

import android.os.Build
import androidx.annotation.RequiresApi
import java.util.Base64
import javax.crypto.Cipher
import javax.crypto.SecretKey
import javax.crypto.spec.IvParameterSpec
import javax.crypto.spec.SecretKeySpec


object CryptoManager {

    private var ENCRYPTION_IV: String
    private var ENCRYPTION_KEY: String

    external fun getEncryptionKey(): String
    external fun getEncryptionIv(): String

    init {
        System.loadLibrary("bagpack")
        this.ENCRYPTION_KEY = getEncryptionKey()
        this.ENCRYPTION_IV = getEncryptionIv()
    }

    @RequiresApi(Build.VERSION_CODES.O)
    fun encrypt(input: ByteArray): String? {
        val cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING")
        val secretKey: SecretKey = SecretKeySpec(ENCRYPTION_KEY.toByteArray(), "AES")
        cipher.init(Cipher.ENCRYPT_MODE, secretKey, IvParameterSpec(ENCRYPTION_IV.toByteArray()))
        return Base64.getEncoder().encodeToString(cipher.doFinal(input))
    }

    @RequiresApi(Build.VERSION_CODES.O)
    fun decrypt(input: ByteArray): ByteArray {
        val cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING")
        val secretKey: SecretKey = SecretKeySpec(ENCRYPTION_KEY.toByteArray(), "AES")
        cipher.init(Cipher.DECRYPT_MODE, secretKey, IvParameterSpec(ENCRYPTION_IV.toByteArray()))
        return cipher.doFinal(Base64.getDecoder().decode(input))
    }
}