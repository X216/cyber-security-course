# Preface
- [What is Infosec?](#infosec)

## What is InfoSec ? {#infosec}

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

### Cyber Criminals (Malicious/Black Hat Hacker)

- **Motivation**: Financial Gain
- **Technique**: Ransomeware Attack, Identity theft, Financial fraud, Data breaches etc.
- **Profile**: Work alone or in loosely connected group
- **Tools**: Use common hacking tools, exploit kits, malware (e.g., ransomware, Trojans), phishing campaigns, and social engineering techniques.

### Hacktivist

- **Motivation**: Political or ideological goal
- **Technique**: DDos Attack, Website defacement, Data Leaks.
- **Profile**: Individual Or With Organised Group.
- **Tools**: 

### Script Kiddies

- **Motivation**: Status, thrill-seeking, or proving their skills
- **Technique**: hese are individuals with limited technical skills who use pre-made scripts, tools, or hacking software created by more skilled attackers. They often engage in low-level attacks like defacing websites or launching simple DDoS attacks.
- **Profile**: Typically, young hackers with limited technical knowledge who aim to gain recognition in hacker communities. Their attacks are often opportunistic and not highly targeted.
- **Tools**: Downloadable hacking tools and publicly available exploits.

### Cybersecurity Researchers (White Hat Hackers)

- **Motivation**: Improving security, ethical hacking
- **Technique**: These are ethical hackers who legally probe systems for vulnerabilities to identify weaknesses before malicious actors exploit them. They help organizations improve their defenses and security posture.
- **Profile**: Typically individuals or teams working independently or for organizations to test and enhance cybersecurity measures. Their goal is to protect systems rather than exploit them.
- **Tools**: Penetration testing tools, vulnerability scanners, reverse engineering, and other ethical hacking methodologies.

### Crackers

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

## Security Governance

Security governance refers to the framework of policies, standards, and guidelines that guide an organization’s approach to managing and securing its information systems, data, and IT infrastructure. It ensures that security is an integral part of business operations, risks are managed effectively, and compliance requirements are met. Here's an overview of the key components of security governance:

1. **Policies**: A security policy is a high-level document that outlines an organization’s approach to security and sets the direction for security practices and controls across the entire organization.
2. **Standards**: Security standards are specific, mandatory rules and criteria that ensure systems and processes adhere to established security practices. Standards provide technical and operational details on how security should be implemented.
3. **Guidelines**: Security guidelines are recommended practices and suggestions for implementing security controls and policies. Unlike standards, guidelines are not mandatory but provide practical advice and recommendations based on best practices.

## Risk Management Frameworks

Risk management frameworks (RMFs) provide structured approaches to identifying, assessing, managing, and monitoring risks within an organization. They are essential for ensuring that an organization's information systems and data are secure, compliant with regulations, and able to handle potential threats.
There are two widely used risk management framework is:

### NIST Risk Management Framework 

The NIST Risk Management Framework (RMF) is a comprehensive approach designed to manage and mitigate risks to organizational assets, particularly in the context of federal agencies and other sectors requiring high security. NIST RMF provides guidelines for risk-based decision-making, system security, and continuous monitoring. It is mainly focused on managing the security and privacy risks of information systems.

### ISO/IEC 27001: Information Security Management System (ISMS)

ISO/IEC 27001 is an international standard that outlines the requirements for establishing, implementing, operating, monitoring, reviewing, maintaining, and improving an Information Security Management System (ISMS). The goal is to protect the confidentiality, integrity, and availability of information by applying a risk management process.
ISO/IEC 27001 provides a systematic approach to managing sensitive company information, ensuring that it remains secure. It is one of the most widely used frameworks for information security governance.

## Laws And Regulations: GDPR and HIPAA

Laws and regulations are critical for guiding organizations in the responsible handling of sensitive data and ensuring that individuals’ rights are respected. GDPR (General Data Protection Regulation) and HIPAA (Health Insurance Portability and Accountability Act) are two major regulations that govern data privacy and protection in specific sectors. Both aim to protect individuals’ personal information but focus on different industries and regions. Below is an in-depth explanation of each:

### GDPR (General Data Protection Regulation)

GDPR is a comprehensive data protection law in the European Union (EU) that was implemented on May 25, 2018. It was designed to enhance and unify data protection for individuals within the EU, ensuring greater control over their personal data and establishing strong penalties for violations.
- Applies to any organization (inside or outside the EU) that processes the personal data of individuals who are located in the EU, regardless of the organization's location.
- Covers all personal data, which includes any information related to an identified or identifiable natural person, such as names, emails, IP addresses, biometric data, and more.

###  HIPAA (Health Insurance Portability and Accountability Act)

HIPAA is a U.S. law, enacted in 1996, aimed at ensuring the privacy and security of health information. It primarily governs healthcare organizations, such as hospitals, healthcare providers, insurance companies, and their business associates, to ensure the confidentiality and integrity of protected health information (PHI).

## Ethical Hacking Vs Malicious Hacking

| Aspect | Ethical Hacking | Malicious Hacking |
| -----: | :-------------: | :---------------- |
| Permission | Conducted with explicit permission from the system owner. | No permission, coducted illegaly |
| Goal | To improve security by identifying and fixing vulnerabilities. | To exploit vulnerabilities |
| Methods | Uses the same techniques as malicious hackers but for a legitimate purpose. | Uses techniques to exploit systems and gain unauthorized access. |
| Outcome | Results in improved security and protection of systems. | Lead of Data breaches, Financial Lost, Physical Loss |
| Legality | Legal and regulated under laws like GDPR, HIPAA, and others. | Illegal and violates laws such as the Computer Fraud and Abuse Act (CFAA). |
| Reporting | Ethical hackers report vulnerabilities to the organization and help patch them. | Exploit the vulnerabilities |
| Accountability | Ethical hackers are accountable for their actions and follow agreed-upon terms and contracts. | Malicious Hackers are conceal their identity to avoid detection. |
| Examples | Penetration testing, vulnerability assessments, bug bounty programs. | Ransomware attacks, data theft, DDoS attacks, identity theft. |

## Professional Ethics And Code Of Conduct

Professional ethics and code of conduct refer to the set of moral principles and rules that guide the behavior and practices of professionals in a given field. These frameworks ensure that professionals act in ways that maintain public trust, promote fairness, and uphold the integrity of their profession. A clear code of conduct helps professionals understand their responsibilities and obligations to their clients, organizations, and the society at large. In many industries, especially those involving sensitive data or high public trust (like healthcare, law, and cybersecurity), adherence to professional ethics is critical.

**Extra**: Professional ethics and the code of conduct are essential for maintaining integrity, trust, and accountability within any profession. They guide professionals in making ethical decisions, dealing with dilemmas, and fostering a positive work culture. By adhering to these principles, professionals not only protect themselves legally but also contribute to the greater good of their industry and society at large. Whether in healthcare, law, finance, or cybersecurity, these ethical guidelines ensure that professionals serve the best interests of their clients, organizations, and communities.
