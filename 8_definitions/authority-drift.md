# Authority Drift

![Authority Drift Diagram](../assets/authority-drift-v1.png)

**Defined by Yoshimi Nakane**

## Definition

Authority Drift describes the gap between authority that is recorded or assigned, and authority that remains contextually valid, structurally intact, and operationally real as conditions change.

It includes the condition in which formal responsibility remains visible in the record, while the legitimate authority behind the decision has already degraded.

## Core Distinction

Most systems track **who is responsible**.

They do not verify whether authority was still **valid at the moment a decision became executable**.

This creates a structural gap between recorded responsibility and actual authority.

## Structural Problem

Responsibility is typically treated as a static attribute recorded after the fact.

Authority, however, is dynamic and context-dependent.

As a result:

- A decision may appear valid in the record
- While the authority behind it has already become stale, impaired, conflicted, misrecognized, or procedurally preserved after its original conditions changed

This mismatch is not visible in most systems.

## Drift Before the Irreversible Threshold

Authority Drift can begin before the irreversible threshold is reached.

It can begin in how authority is recognized, maintained, and carried forward.

A system may continue to treat a prior assignment as currently valid even when the human, contextual, institutional, or responsibility conditions that made that authority meaningful have changed.

## Relationship to Interruption Authority

Authority Drift is not only a signal of missing interruption authority.

It is one of the conditions that can make interruption authority unreliable in the first place — or reveal why it must be explicitly designed.

Interruption authority asks who can still stop execution.

Authority Drift asks whether the authority being carried into that moment is still legitimate, contextual, and real.

These framings are closely connected, but analytically distinct.

## Failure Mode

Authority Drift represents a primary failure mode in high-stakes decision environments:

- medical decisions executed after cognitive fatigue
- approvals executed after role or scope changes
- AI-influenced recommendations without explicit attribution
- delegated decisions without updated authority validation
- execution continuing after the authority context has become stale or misrecognized

In each case, responsibility remains visible, but the underlying authority condition is no longer intact.

## Implication

A system that records responsibility without verifying authority cannot guarantee that decisions are legitimately executable.

Tracking “who decided” is insufficient.

The system must determine whether authority was valid **at execution time**.

## Relationship to Legitimacy Layer

Authority Drift is the observable symptom of a missing upstream definition.

The Legitimacy Layer defines:

What must be true for human judgment to count as valid authority.

Authority Drift occurs when those conditions degrade before execution, without being detected or revalidated.

## Relationship to Context Refresh Requirement

Context Refresh Requirement asks whether the conditions that made prior authority legitimate still hold before execution becomes consequential.

Authority Drift is more likely when no context refresh occurs between authority assignment and execution.

## Design Principle

Systems must not treat recorded responsibility as proof of valid authority.

They must detect, prevent, or surface Authority Drift before irreversible execution occurs.

## Positioning

Authority Drift is not an error in execution.

It is a structural misalignment between recorded responsibility and actual authority.

It reveals the absence of a legitimacy-aware system design.

## Defined by

Yoshimi Nakane / Human Reference Point™ Framework

## Last Updated

2026-05-14
