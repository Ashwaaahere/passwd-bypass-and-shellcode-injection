Name: Ashwathaman Satish Kumar  
B-Number: B01106017  

---------------------------
Part 1: Bypassing Password Check
---------------------------

Files:
- vuln_program.c     → Vulnerable C program
- attack.py          → Python script to generate 'attack_string'
- attack_string      → Payload to overwrite return address to jump to target()

How to Run:
1. Compile the program:
   gcc -fno-stack-protector -z execstack -fno-pie -no-pie -m32 -O0 -g vuln_program.c -o vuln_program

2. Find the target function address:
   nm vuln_program | grep target
   (e.g., 08049196)

3. Generate the attack string:
   python3 attack.py 08049196

4. Run the vulnerable program with the attack payload:
   ./vuln_program < attack_string

Expected Output:
- Should print: "You have entered the correct passwd"
- Proof of exploit: When tested in GDB, it breaks at the 'target' function.

---------------------------
Part 2: Launching Shell via Shellcode
---------------------------

Files:
- shell_attack.py    → Python script to generate 'shell_string'
- shell_string       → Payload to execute injected shellcode

How to Run:
1. Generate the shell payload:
   python3 shell_attack.py

2. Execute the vulnerable program with ASLR disabled:
   setarch $(uname -m) -R ./vuln_program < shell_string

Expected Output:
- If successful, a `$` shell will appear.
- To exit the shell, type: `exit`

---------------------------
Status
---------------------------

✔️ Part 1: Working as expected (verified via GDB)
✔️ Part 2: Payload constructed and runs with provided shellcode. May require tweaking address using GDB to achieve shell execution.

---------------------------
