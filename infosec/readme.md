## What is InfoSec ?
InfoSec refers to Information Security. Information Security is the process of protecting an organization data from unauthorised access or modification.

## CIA Triad:
There are three main part of InfoSec:
- **Confidentiality**
- **Integrity**
- **Availability**

### Confidentiality
The organization data must be confidential. Only the user can access those data by using a end to end encryption method or 2fa. So, InfoSec secured the organization data.
### Integrity
Integrity means all the data must be valid and proper checked and sanitized. Consistency includes protection against unauthorized changes (additions, deletions, alterations, etc.) to data. It makes the organization trustworthy. So Integrity is one of the most important part of InfoSec.
### Availability
After Confidentiality and Integrity then comes to Availability. Availability is the protection of a system’s ability to make software systems and data fully available when a user needs it (or at a specified time). Users and organization should have run the system without any errors or issues. And the system should be available to use.

## Fundamental Concept Of Security
There are three fundamental concept of security:
- **Vulnerability** : A vulnerability exposes your organization to threats.
- **Threat** : A threat is a malicious or negative event that take advantages of a vulnerability.
- **Risk** : It is the potential loss and damage when the threat does occur.

### Vulnerability
A vulnerability is a weakness, flaw, or other shortcoming in a system(infrastructure, database, or software), but it can also exist in a process,a set of controls, or simply just the way that something has been implemented or deployed.
There are two general type of vulnerabilities:
- **Technical Vulnerabilities**: Bugs in code, error in some hardware or software.
- **Human Vulnerabilities**: Data theft from employee or employee for for phishing.

### Threat
Anything that could exploit or take advantage of vulnerability is called threat. Any malicious or negative that could exploit the vulnerability is also called threat. Some common threats are:
- Malware
- Advance Persistent Threats (APIs)
- Social Engineering Attack
- Ransomware Attack
- Zero-Day Vulnerabilities
- Human Error

### Risk
For vulnerability and threat the potential physical or digital loss is called risk. The calculation of risk is depend on threat and vulnerability. We can calculate or assume total risk by multiply vulnerability with threat.
```python
risk = vulnerability * threat
```

## Cyber Threat Landscape
The cyber threat landscape refers to the evolving environment of potential cyber threats, risks, and vulnerabilities that organizations and individuals face in the digital world. It encompasses the various types of cyberattacks, tactics, techniques, and procedures (TTPs) that cybercriminals, hackers, hacktivists, nation-states, and other malicious actors employ to compromise systems, steal data, or disrupt operations.

**[Cyber Threat Landscape Report 2022](https://www.unicc.org/wp-content/uploads/2023/05/UNICC-Cyber-Threat-Landscape-Report-2022.pdf)**

## Types Of Attackers
1. **Cyber Criminals (Malicious/Black Hat Hacker)**: 
- **Motivation**: Financial Gain
- **Technique**: Ransomeware Attack, Identity theft, Financial fraud, Data breaches etc.
- **Profile**: Work alone or in loosely connected group
- **Tools**: Use common hacking tools, exploit kits, malware (e.g., ransomware, Trojans), phishing campaigns, and social engineering techniques.

2. **Hacktivist**: 
- **Motivation**: Political or ideological goal
- **Technique**: DDos Attack, Website defacement, Data Leaks.
- **Profile**: Individual Or With Organised Group.
- **Tools**: 

3. **Script Kiddies**: 
- **Motivation**: Status, thrill-seeking, or proving their skills
- **Technique**: hese are individuals with limited technical skills who use pre-made scripts, tools, or hacking software created by more skilled attackers. They often engage in low-level attacks like defacing websites or launching simple DDoS attacks.
- **Profile**: Typically, young hackers with limited technical knowledge who aim to gain recognition in hacker communities. Their attacks are often opportunistic and not highly targeted.
- **Tools**: Downloadable hacking tools and publicly available exploits.

4. **Cybersecurity Researchers (White Hat Hackers)**: 
- **Motivation**: Improving security, ethical hacking
- **Technique**: These are ethical hackers who legally probe systems for vulnerabilities to identify weaknesses before malicious actors exploit them. They help organizations improve their defenses and security posture.
- **Profile**: Typically individuals or teams working independently or for organizations to test and enhance cybersecurity measures. Their goal is to protect systems rather than exploit them.
- **Tools**: Penetration testing tools, vulnerability scanners, reverse engineering, and other ethical hacking methodologies.

5. **Crackers**: 
- **Motivation**: Malicious intent, personal gain, revenge, or financial profit
- **Technique**: Crackers focus on bypassing or defeating security mechanisms like passwords, encryption, and licensing protections. Their activities can range from cracking software protections to breaking into systems for data theft or sabotage.
- **Profile**: Crackers are often skilled in various aspects of cybersecurity but use their knowledge to exploit vulnerabilities for harmful purposes. Unlike ethical hackers, their actions are illegal and aimed at bypassing protections, rather than improving security.
- **Tools**: Crackers typically use tools like brute-force password crackers, exploit kits, keyloggers, and malware (e.g., rootkits and Trojans). They may also use reverse engineering techniques to bypass software protections or uncover flaws in systems.

## Some common attack vectors
- **Phishing**: Phishing is an attack where the attacker gain the trustworthy entity to trick the individuals and get their personal password or data.
- **Malware**: Any Software design to gain unauthorised access in the system. In includes `viruses`,`ransomware`,`worms`,`trojans`,`Spyware` etc.
- **Social Engineering**: Social engineering involves manipulating individuals into divulging confidential or personal information by exploiting human psychology rather than technical vulnerabilities.
- **Man-in-the-middle(MitM) Attacks**:  In a Man-in-the-Middle attack, the attacker intercepts and possibly alters communication between two parties (victims) without their knowledge. This can happen on unsecured networks (e.g., public Wi-Fi).
- **SQL Injection**:  SQL injection is a technique where an attacker exploits a vulnerability in an application’s database query mechanism. They inject malicious SQL code into input fields (e.g., login forms) to manipulate the database.
- **Cross Site Scripting(XSS)**: XSS occurs when an attacker injects malicious scripts into content that is viewed by other users (typically within web browsers). These scripts are often used to steal session cookies or redirect users to malicious sites.
