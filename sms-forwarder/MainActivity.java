import android.Manifest;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;
import android.telephony.SmsManager;
import android.database.Cursor;
import android.net.Uri;

public class MainActivity extends AppCompatActivity {
    private static final int READ_SMS_PERMISSION_CODE = 1;
    private static final int SEND_SMS_PERMISSION_CODE = 2;
    
    private EditText phoneNumberEditText;
    private Button forwardButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phoneNumberEditText = findViewById(R.id.phone_number_edit_text);
        forwardButton = findViewById(R.id.forward_button);

        forwardButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (checkPermission(Manifest.permission.READ_SMS, READ_SMS_PERMISSION_CODE) &&
                    checkPermission(Manifest.permission.SEND_SMS, SEND_SMS_PERMISSION_CODE)) {
                    forwardSMS();
                }
            }
        });
    }

    private boolean checkPermission(String permission, int requestCode) {
        if (ContextCompat.checkSelfPermission(this, permission) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this, new String[]{permission}, requestCode);
            return false;
        }
        return true;
    }

    private void forwardSMS() {
        String phoneNumber = phoneNumberEditText.getText().toString();

        if (phoneNumber.isEmpty()) {
            Toast.makeText(this, "Enter a valid phone number", Toast.LENGTH_SHORT).show();
            return;
        }

        // Read SMS messages
        Uri uri = Uri.parse("content://sms/inbox");
        Cursor cursor = getContentResolver().query(uri, null, null, null, null);

        if (cursor != null) {
            while (cursor.moveToNext()) {
                String sender = cursor.getString(cursor.getColumnIndex("address"));
                String message = cursor.getString(cursor.getColumnIndex("body"));

                // Forward SMS to the specified phone number
                sendSMS(phoneNumber, sender, message);
            }
            cursor.close();
        } else {
            Toast.makeText(this, "Failed to read SMS messages", Toast.LENGTH_SHORT).show();
        }

        Toast.makeText(this, "SMS messages forwarded", Toast.LENGTH_SHORT).show();
    }

    private void sendSMS(String phoneNumber, String sender, String message) {
        SmsManager smsManager = SmsManager.getDefault();
        String forwardedMessage = "From: " + sender + "\n" + message;
        smsManager.sendTextMessage(phoneNumber, null, forwardedMessage, null, null);
    }

    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if (requestCode == READ_SMS_PERMISSION_CODE || requestCode == SEND_SMS_PERMISSION_CODE) {
            if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                forwardSMS();
            } else {
                Toast.makeText(this, "Permission denied", Toast.LENGTH_SHORT).show();
            }
        }
    }
}
