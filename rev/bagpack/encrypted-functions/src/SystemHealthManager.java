package com.siahaan.shm;

import android.content.ContentResolver;
import android.os.Build;
import android.provider.Settings;

import java.nio.charset.StandardCharsets;
import java.util.Base64;

public class SystemHealthManager {
    public static char[] base64Decode(String base64EncodedString) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
            byte[] result = Base64.getDecoder().decode(base64EncodedString.getBytes(StandardCharsets.UTF_8));
            return new String(result, StandardCharsets.UTF_8).toCharArray();
        }
        return null;
    }

    public static String base64Encode(String input) {
        byte[] encodedBytes = new byte[0];
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            encodedBytes = Base64.getEncoder().encode(input.getBytes());
        }

        return new String(encodedBytes);
    }

    public void run(ContentResolver contentResolver) {
        System.out.println("Invoking...");
        System.out.println("Note: This is experimental. Only I should be able to run this code.");
        String mId = Settings.Secure.getString(contentResolver, Settings.Secure.ANDROID_ID);
        System.out.println("ID: " + mId);

        if (mId.equals("377592fe959bca52")) {
            char[] inputChars = base64Decode("f3xkTl1dFFFmV1gBCD5YS2xVVlJmA1ZUCQQJUFMc");
            char[] keyChars = mId.toCharArray();

            for (int i = 0; i < inputChars.length; i++) {
                inputChars[i] = (char)(inputChars[i] ^ keyChars[i % keyChars.length]);
            }

            String b = new String(inputChars);
            // System.out.println("Flag: " + b);
        }
    }
}