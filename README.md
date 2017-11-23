# OBD-II Skill for Mycroft AI
by Weltgeist, November-21-2017

This skill will give Mycroft knowledge about OBD-II PID codes. It is intended to help you diagonse your vehicle. This use case of this skill may change in the future.

This is part of a broader project to bring Mycroft into the automotive world.

## Usage

### To start
> "Hey Mycroft, diagnose a vehicle."

## Example Session
"Hey Mycroft, diagnose a car."

"What is the make of the car?"

"Subaru."

"The make you have specified is Subaru, is this correct?"

"Yes."

"What is your OBD-2 code?"

"P0011."

"P0011 means Camshaft Position 'A' Timing Over Advance or Performance Bank. Do you want to know more?"

"Yes."

"Here are some possible causes: Low or Dirty Engine Oil, Timing belt misaligned, Faulty AVCS solenoid. Do you want to know more?"

"Yes."

"Here are some possible symptoms: Engine Light ON (or Service Engine Soon Warning Light), Lack/Loss of power, Engine noise, Engine rough idle. Do you want to know more?"

"Yes."

"The Engine Control Module (ECM) controls the Oil Control Valve (OCV) to regulate the intake camshaft angle. As a result of the angle change, the engine timing is advance or retard. Optimizing engine timing will help the engine improve torque and fuel economy, and the exhaust emissions decrease under overall driving conditions. The Variable Valve Timing (VVT) system includes the Oil Control Valve (OCV) and VVT controller. The ECM detects the actual intake valve timing using signals from the camshaft and crankshaft position sensors, and performs feedback control. That is all the information I have."


## OBD-II PID sources
- https://www.autocodes.com/
- https://www.obd-codes.com/
