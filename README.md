# Biometric Fingerprint Reader
At the university along with my team decided to build a fingerprint reader with a GUI interface to show out the users signed up
whenever they get authenticated using the device. So we thought that'd be interesting to mix **Python** with **C++** in **Arduino**
enviroment via *serial* communication. Throughout this doc you will see the performance of this small project but complex too. 

## Getting started
This project is oriented to people who is interested in how it works this project which is a simplification of a real world security
system in a company or wherever location you consider properly.

---

### Requirements
The biometric sensor required for this project is the `Fpm10a` microcontroller 
([See its datasheet](https://artofcircuits.com/product/fpm10a)).

<img src="https://camo.githubusercontent.com/a1e7a6c7d447062cde405f47d2cfca7082815c6f557e9118b4cb073589d86e12/68747470733a2f2f63646e2d73686f702e61646166727569742e636f6d2f393730783732382f3735312d30332e6a7067" width="350" height="300">

Since this sensor works using serial communication through a port, Python can establish a connection with it by using the __serial__ 
module, so that is required; otherwise, the script won't be able to communicate to the microcontroller.

Besides, the C++ code needs to work with a library that provides all the tools for authentication and registering. This library
is called _Adafruit-Fingerprint-Sensor_ and you can visit the repo [by clicking on this link](https://github.com/adafruit/Adafruit-Fingerprint-Sensor-Library.git). This library offers you a set of examples to you learn to use this library.

Finally, you might need an **Arduino uno** to load and run the C++ code.

> Don't worry about the C++ code, almost all the code wasn't modified for this project.

### Low-code structure
The project contains two folders with C++ code:

* `enroll.ino`
* `fingerprint.ino`

Inside of these folders you can find the same files that the Adafruit framework has in its examples files. But, it's recommended to use this files
beacuse the code is written by the creators themselves which is great. How ever, if you want to know what's happening under the hood of that code,
be free to take a look at the files.

Well, the purpose of these files is _saving new fingerprints_ and _authenticating_ the fingerprint desired; so _Enroll_ and _Fingerprint_ files
takes care of this two functions respectively. Always you want to save new fingerprints, you'll need to run `enroll.ino` either in the Arduino IDE 
or any other IDE able to run `.ino` files. During the runtime of these files, you're going to be seeing on the _serial console_ the steps to follow to enroll new fingerprints and get authenticated with the already saved ones.

### Data-structure 
Now you need to save the users' data into a database, so in this case the database is performed by a simple **JSON** file which is easy to use and
uses a standard data model, so even you can use the data into other applications that consumes the same database. You can find this json file in
`/database/database.json`, in caso you want to change this name, you'll need to change it in the connection of `Database.py` at the end of the code.

An exmaple of the structure of the data is the following which can be found in the sheets:

```json
[
  {
    "id": 13,
    "name": "User",
    "code": "123456789",
    "age": 21,
    "carrer": "Computer science",
    "semester": 4,
    "photo": "./images/user.jpg"
  },
]
```

This structure was taken from the university where I study, so that information is what I should to include in. How ever, if you want to include
other information, you can do it, because the information is indexed by the `id` key. 

### Authentication
Once everything is mounted in working correctly, you might want to test you fingerprint after enrolling it. You'll have to run `fingerprint.ino` and
logically `Board.py` for creating a connection with the serial port (ensure devices port and the passed as argument in Python match, look at 
Arduino IDE for serial ports available). Then put your finger over the sensor and see what happens in the console; it's probable the sensor fails 
sometimes at matching. When the sensor detects a enrolled finger, it will automatically display a screen with all the saved user's information.

You can overview the usage of the device with the saved data.
[Fingerprint reader usage](https://youtu.be/CyLK2_s7_fM)
