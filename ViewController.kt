import android.bluetooth.BluetoothAdapter
import android.bluetooth.BluetoothDevice
import android.bluetooth.BluetoothGatt
import android.bluetooth.BluetoothGattCallback
import android.bluetooth.BluetoothGattCharacteristic
import android.bluetooth.BluetoothGattService
import android.bluetooth.BluetoothManager
import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.View
import android.widget.Button
import android.widget.ImageView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    private lateinit var bluetoothAdapter: BluetoothAdapter
    private lateinit var bluetoothGatt: BluetoothGatt
    private lateinit var ledSendChar: BluetoothGattCharacteristic
    private lateinit var ledReadState: BluetoothGattCharacteristic
    private lateinit var savedPeripheral: BluetoothDevice
    private var led = false

    private val arduinoSvc = "0000DF01-0000-1000-8000-00805F9B34FB"
    private val arduinoLEDchar = "0000DF02-0000-1000-8000-00805F9B34FB"
    private val arduinoLEDstate = "0000DF03-0000-1000-8000-00805F9B34FB"

    private lateinit var btStatus: ImageView
    private lateinit var stopBtn: Button
    private lateinit var fwdBtn: Button
    private lateinit var bckBtn: Button
    private lateinit var rBtn: Button
    private lateinit var lBtn: Button
    private lateinit var stndBtn: Button
    private lateinit var sqtBtn: Button
    private lateinit var wvlBtn: Button
    private lateinit var wvrBtn: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btStatus = findViewById(R.id.btStatus)
        stopBtn = findViewById(R.id.stopBtn)
        fwdBtn = findViewById(R.id.fwdBtn)
        bckBtn = findViewById(R.id.bckBtn)
        rBtn = findViewById(R.id.rBtn)
        lBtn = findViewById(R.id.lBtn)
        stndBtn = findViewById(R.id.stndBtn)
        sqtBtn = findViewById(R.id.sqtBtn)
        wvlBtn = findViewById(R.id.wvlBtn)
        wvrBtn = findViewById(R.id.wvrBtn)

        val bluetoothManager = getSystemService(Context.BLUETOOTH_SERVICE) as BluetoothManager
        bluetoothAdapter = bluetoothManager.adapter

        stopBtn.setOnClickListener {
            Log.d("MainActivity", "Stop Button Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(69.toByte()))
        }

        fwdBtn.setOnClickListener {
            Log.d("MainActivity", "Up Button Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(65.toByte()))
        }

        bckBtn.setOnClickListener {
            Log.d("MainActivity", "Backwards Button Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(66.toByte()))
        }

        rBtn.setOnClickListener {
            Log.d("MainActivity", "Right Button Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(70.toByte()))
        }

        lBtn.setOnClickListener {
            Log.d("MainActivity", "Left Button Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(71.toByte()))
        }

        stndBtn.setOnClickListener {
            Log.d("MainActivity", "Stand Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(115.toByte()))
        }

        sqtBtn.setOnClickListener {
            Log.d("MainActivity", "Squat Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(113.toByte()))
        }

        wvlBtn.setOnClickListener {
            Log.d("MainActivity", "Wave Left Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(108.toByte()))
        }

        wvrBtn.setOnClickListener {
            Log.d("MainActivity", "Wave Right Clicked")
            savedPeripheral.writeCharacteristic(ledSendChar, byteArrayOf(114.toByte()))
        }
    }

    override fun onResume() {
        super.onResume()
        val bluetoothLeScanner = bluetoothAdapter.bluetoothLeScanner
        bluetoothLeScanner.startScan(null, null, scanCallback)
    }

    override fun onPause() {
        super.onPause()
        bluetoothAdapter.bluetoothLeScanner.stopScan(scanCallback)
    }

    private val scanCallback = object : BluetoothAdapter.LeScanCallback {
        override fun onLeScan(device: BluetoothDevice?, rssi: Int, scanRecord: ByteArray?) {
            if (device?.name?.contains("ESP") == true) {
                savedPeripheral = device
                bluetoothAdapter.bluetoothLeScanner.stopScan(this)
                device.connectGatt(this@MainActivity, false, gattCallback)
            }
        }
    }

    private val gattCallback = object : BluetoothGattCallback() {
        override fun onConnectionStateChange(gatt: BluetoothGatt?, status: Int, newState: Int) {
            if (newState == BluetoothGatt.STATE_CONNECTED) {
                gatt?.discoverServices()
            }
        }

        override fun onServicesDiscovered(gatt: BluetoothGatt?, status: Int) {
            val services: List<BluetoothGattService> = gatt?.services ?: return
            for (service in services) {
                if (service.uuid.toString() == arduinoSvc) {
                    val characteristics: List<BluetoothGattCharacteristic> = service.characteristics
                    for (characteristic in characteristics) {
                        if (characteristic.uuid.toString() == arduinoLEDchar) {
                            ledSendChar = characteristic
                        } else if (characteristic.properties and BluetoothGattCharacteristic.PROPERTY_NOTIFY != 0) {
                            ledReadState = characteristic
                            gatt.setCharacteristicNotification(characteristic, true)
                        }
                    }
                }
            }
        }

        override fun onCharacteristicChanged(
            gatt: BluetoothGatt?,
            characteristic: BluetoothGattCharacteristic?
        ) {
            if (characteristic?.uuid.toString() == arduinoLEDstate) {
                val value = characteristic.value[0]
                val pz = value.toChar()
                Log.d("MainActivity", "Received value '$pz' from the ESP32")
                when (pz) {
                    'N' -> {
                        led = true
                        Log.d("MainActivity", "LED is on")
                    }
                    'X' -> {
                        led = false
                        Log.d("MainActivity", "LED is off")
                    }
                    'R' -> {
                        led = false
                        Log.d("MainActivity", "Toaster is ready")
                    }
                }
            }
        }

        override fun onCharacteristicWrite(
            gatt: BluetoothGatt?,
            characteristic: BluetoothGattCharacteristic?,
            status: Int
        ) {
            Log.d("MainActivity", "Wrote value to ESP32")
        }
    }
}


