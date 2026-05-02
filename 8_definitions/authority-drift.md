# Authority Drift
**Defined by Yoshimi Nakane**

## Definition
Authority Drift is the condition in which formal responsibility remains visible in the record,  
while the legitimate authority behind the decision has already degraded.

---

## Core Distinction
Most systems track **who is responsible**.  
They do not verify whether authority was still **valid at the moment a decision became executable**.

This creates a structural gap between recorded responsibility and actual authority.

---

## Structural Problem
Responsibility is typically treated as a static attribute recorded after the fact.  
Authority, however, is dynamic and context-dependent.

As a result:

- A decision may appear valid in the record  
- While the authority behind it has already become stale, impaired, or conflicted  

This mismatch is not visible in most systems.

---

## Failure Mode
Authority Drift represents a primary failure mode in high-stakes decision environments:

- medical decisions executed after cognitive fatigue  
- approvals executed after role or scope changes  
- AI-influenced recommendations without explicit attribution  
- delegated decisions without updated authority validation  

In each case, responsibility remains visible,  
but the underlying authority condition is no longer intact.

---

## Implication
A system that records responsibility without verifying authority  
cannot guarantee that decisions are legitimately executable.

Tracking “who decided” is insufficient.  
The system must determine whether authority was valid **at execution time**.

---

## Relationship to Legitimacy Layer
Authority Drift is the observable symptom of a missing upstream definition.

The Legitimacy Layer defines:
What must be true for human judgment to count as valid authority.

Authority Drift occurs when those conditions degrade  
before execution, without being detected or revalidated.

---

## Design Principle
Systems must not treat recorded responsibility as proof of valid authority.

They must detect, prevent, or surface Authority Drift  
before irreversible execution occurs.

---

## Positioning
Authority Drift is not an error in execution.  
It is a structural misalignment between recorded responsibility and actual authority.

It reveals the absence of a legitimacy-aware system design.
