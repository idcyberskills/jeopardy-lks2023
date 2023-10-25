package com.siahaan.bagpack.activities;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import androidx.appcompat.app.AppCompatActivity;
import androidx.fragment.app.FragmentActivity;
import com.bumptech.glide.Glide;
import com.google.firebase.FirebaseApp;
import com.siahaan.bagpack.R;
import com.siahaan.bagpack.utils.FirebaseStorageManager;
import kotlin.Metadata;
import kotlin.jvm.internal.Intrinsics;
import kotlinx.coroutines.BuildersKt__BuildersKt;

/* compiled from: MainActivity.kt */
@Metadata(d1 = {"\u0000 \n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0010\u0002\n\u0000\n\u0002\u0018\u0002\n\u0002\b\u0002\n\u0002\u0018\u0002\n\u0000\u0018\u00002\u00020\u0001B\u0005¢\u0006\u0002\u0010\u0002J\u0012\u0010\u0003\u001a\u00020\u00042\b\u0010\u0005\u001a\u0004\u0018\u00010\u0006H\u0015J\u000e\u0010\u0007\u001a\u00020\u00042\u0006\u0010\b\u001a\u00020\t¨\u0006\n"}, d2 = {"Lcom/siahaan/bagpack/activities/MainActivity;", "Landroidx/appcompat/app/AppCompatActivity;", "()V", "onCreate", "", "savedInstanceState", "Landroid/os/Bundle;", "show", "view", "Landroid/view/View;", "app_release"}, k = 1, mv = {1, 6, 0}, xi = 48)
/* loaded from: classes.dex */
public final class MainActivity extends AppCompatActivity {
    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        requestWindowFeature(1);
        getWindow().setFlags(1024, 1024);
        FirebaseApp.initializeApp(this);
        setContentView(R.layout.activity_main);
        setTitle("Bag My Pack");
        BuildersKt__BuildersKt.runBlocking$default(null, new MainActivity$onCreate$1(new FirebaseStorageManager(), this, null), 1, null);
    }

    public final void show(View view) {
        Intrinsics.checkNotNullParameter(view, "view");
        View findViewById = findViewById(R.id.imageView);
        Intrinsics.checkNotNullExpressionValue(findViewById, "findViewById(R.id.imageView)");
        Glide.with((FragmentActivity) this).mo229load(Integer.valueOf((int) R.drawable.warp)).into((ImageView) findViewById);
        view.setVisibility(8);
    }
}