package com.siahaan.bagpack.utils;

import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlin.text.Charsets;

/* compiled from: CryptoManager.kt */
@Metadata(d1 = {"\u0000\u001c\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0002\b\u0002\n\u0002\u0010\u000e\n\u0002\b\u0002\n\u0002\u0010\u0012\n\u0002\b\u0005\bÆ\u0002\u0018\u00002\u00020\u0001B\u0007\b\u0002¢\u0006\u0002\u0010\u0002J\u0010\u0010\u0006\u001a\u00020\u00072\u0006\u0010\b\u001a\u00020\u0007H\u0007J\u0012\u0010\t\u001a\u0004\u0018\u00010\u00042\u0006\u0010\b\u001a\u00020\u0007H\u0007J\t\u0010\n\u001a\u00020\u0004H\u0086 J\t\u0010\u000b\u001a\u00020\u0004H\u0086 R\u000e\u0010\u0003\u001a\u00020\u0004X\u0082\u000e¢\u0006\u0002\n\u0000R\u000e\u0010\u0005\u001a\u00020\u0004X\u0082\u000e¢\u0006\u0002\n\u0000¨\u0006\f"}, d2 = {"Lcom/siahaan/bagpack/utils/CryptoManager;", "", "()V", "ENCRYPTION_IV", "", "ENCRYPTION_KEY", "decrypt", "", "input", "encrypt", "getEncryptionIv", "getEncryptionKey", "app_release"}, k = 1, mv = {1, 6, 0}, xi = 48)
/* loaded from: classes.dex */
public final class CryptoManager {
    private static String ENCRYPTION_IV;
    private static String ENCRYPTION_KEY;
    public static final CryptoManager INSTANCE;

    public final native String getEncryptionIv();

    public final native String getEncryptionKey();

    private CryptoManager() {
    }

    static {
        CryptoManager cryptoManager = new CryptoManager();
        INSTANCE = cryptoManager;
        System.loadLibrary("bagpack");
        ENCRYPTION_KEY = cryptoManager.getEncryptionKey();
        ENCRYPTION_IV = cryptoManager.getEncryptionIv();
    }

    public final String encrypt(byte[] input) {
        Intrinsics.checkNotNullParameter(input, "input");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        byte[] bytes = ENCRYPTION_KEY.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes, "this as java.lang.String).getBytes(charset)");
        byte[] bytes2 = ENCRYPTION_IV.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes2, "this as java.lang.String).getBytes(charset)");
        cipher.init(1, new SecretKeySpec(bytes, "AES"), new IvParameterSpec(bytes2));
        return Base64.getEncoder().encodeToString(cipher.doFinal(input));
    }

    public final byte[] decrypt(byte[] input) {
        Intrinsics.checkNotNullParameter(input, "input");
        Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5PADDING");
        byte[] bytes = ENCRYPTION_KEY.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes, "this as java.lang.String).getBytes(charset)");
        byte[] bytes2 = ENCRYPTION_IV.getBytes(Charsets.UTF_8);
        Intrinsics.checkNotNullExpressionValue(bytes2, "this as java.lang.String).getBytes(charset)");
        cipher.init(2, new SecretKeySpec(bytes, "AES"), new IvParameterSpec(bytes2));
        byte[] doFinal = cipher.doFinal(Base64.getDecoder().decode(input));
        Intrinsics.checkNotNullExpressionValue(doFinal, "cipher.doFinal(Base64.getDecoder().decode(input))");
        return doFinal;
    }
}