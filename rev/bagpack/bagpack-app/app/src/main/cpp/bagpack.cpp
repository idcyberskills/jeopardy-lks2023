#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_siahaan_bagpack_utils_CryptoManager_getEncryptionKey(JNIEnv *env, jobject instance) {
        // Retrieve and return the stored API key
        return env->NewStringUTF("M9qSJqhFCKRsgIY0");
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_siahaan_bagpack_utils_CryptoManager_getEncryptionIv(JNIEnv *env, jobject instance) {
        // Retrieve and return the stored API key
        return env->NewStringUTF("lYpQVWW1fOs2rVFX");
}