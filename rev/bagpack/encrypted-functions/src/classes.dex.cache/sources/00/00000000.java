package com.siahaan.shm;

import android.content.ContentResolver;
import android.os.Build;
import android.provider.Settings;
import java.nio.charset.StandardCharsets;
import java.util.Base64;

/* loaded from: /Users/chrisandoryan/Documents/Work/LKS/LKSN2023/Challenges/LKSN-2023-Challs/bagpack/encrypted-functions/src/classes.dex */
public class SystemHealthManager {
    public static char[] base64Decode(String str) {
        if (Build.VERSION.SDK_INT >= 26) {
            return new String(Base64.getDecoder().decode(str.getBytes(StandardCharsets.UTF_8)), StandardCharsets.UTF_8).toCharArray();
        }
        return null;
    }

    public static String base64Encode(String str) {
        byte[] bArr = new byte[0];
        if (Build.VERSION.SDK_INT >= 26) {
            bArr = Base64.getEncoder().encode(str.getBytes());
        }
        return new String(bArr);
    }

    public void run(ContentResolver contentResolver) {
        System.out.println("Invoking...");
        System.out.println("Note: This is experimental. Only I should be able to run this code.");
        String string = Settings.Secure.getString(contentResolver, "android_id");
        System.out.println("ID: " + string);
        if (string.equals("377592fe959bca52")) {
            char[] base64Decode = base64Decode("f3xkTl1dFFFmV1gBCD5YS2xVVlJmA1ZUCQQJUFMc");
            char[] charArray = string.toCharArray();
            for (int i = 0; i < base64Decode.length; i++) {
                base64Decode[i] = (char) (base64Decode[i] ^ charArray[i % charArray.length]);
            }
            System.out.println("Flag: " + new String(base64Decode));
        }
    }
}