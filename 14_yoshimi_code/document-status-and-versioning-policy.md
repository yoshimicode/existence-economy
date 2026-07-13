# YOSHIMI Code Document Status and Versioning Policy

**Version:** v0.1  
**Effective Date:** 2026-07-11  

## Purpose

This policy prevents hypotheses, direction statements, definitions, specifications, and historical records from being confused with one another.

## Document Status Labels

Every YOSHIMI Code document must display one of the following status labels near the beginning of the file.

### Working Hypothesis

An unverified idea or structure recorded before sufficient research or validation.

A Working Hypothesis must not be described as an established definition, specification, standard, or proven method.

### Direction Statement

A dated record of the direction being considered at a specific point in time.

A Direction Statement preserves the emergence and development of a concept. It does not by itself establish a formal definition.

### Research Record

A record of sources, comparisons, findings, unresolved questions, and limitations produced through research.

A Research Record may support later definitions or specifications but does not automatically become one.

### Formal Definition

A document that states the official meaning and scope of a concept after research and internal review.

A Formal Definition must identify its version, effective date, scope, exclusions, and relationship with earlier documents.

### Formal Specification

A document that defines the components, requirements, interfaces, procedures, or implementation conditions of a system or methodology.

A Formal Specification must be issued separately from a Direction Statement.

### Editorial Principle

A rule governing interpretation, evidence, publication, correction, responsibility, objections, privacy, or protection of affected persons.

### Historical Record

A preserved document that records an earlier state of thought, practice, or development.

Historical Records are retained even when later documents supersede their content.

### Superseded

A document that has been replaced for current operational use by a later document.

A superseded document remains available as part of the historical record and must link to its successor where possible.

## Versioning Rules

- `v0.x` indicates a hypothesis, draft, direction statement, or pre-specification document.
- `v1.0` indicates the first formally adopted version of a definition, specification, or policy.
- Minor versions such as `v1.1` indicate additions or clarifications that do not change the document's central meaning.
- Major versions such as `v2.0` indicate substantive changes to scope, architecture, interpretation, or operation.
- A new version must be added as a new file when it changes the historical meaning of an earlier direction statement.
- Published direction statements and historical records must not be silently overwritten.
- Typographical corrections may be committed to the same file when they do not alter substantive meaning.
- Every substantive revision must be traceable through Git history and, where appropriate, through a revision note in the document.

## File Naming Rules

Use lowercase ASCII filenames with hyphens.

Recommended patterns:

- `yoshimi-code-recognition-os-direction-v0.1.ja.md`
- `yoshimi-code-recognition-os-direction-v0.1.en.md`
- `yoshimi-code-formal-definition-v1.0.ja.md`
- `yoshimi-code-formal-definition-v1.0.en.md`
- `yoshimi-code-concept-architecture-v1.0.md`
- `yoshimi-code-editorial-principles-v1.0.md`

Language suffixes:

- `.ja.md` for Japanese
- `.en.md` for English

The Japanese version is canonical unless a document explicitly states otherwise.

## Repository Separation Rules

Direction statements, formal definitions, and formal specifications must be separate files.

A later formal document may cite an earlier direction statement, but it must not rename the earlier document as if the earlier document had always been formal.

Recommended structure:

- Direction Statements
- Research Records
- Formal Definitions
- Formal Specifications
- Editorial Principles
- Architecture
- Roadmaps
- Historical Records

The initial implementation may use a single `14_yoshimi_code` directory. Subdirectories may be introduced when the number of documents makes status separation necessary.

## README Representation

README links must display the document status and version.

Example:

- YOSHIMI Code Recognition OS Direction Statement v0.1 — Working Hypothesis recorded on 2026-07-11

README text must not present a `v0.x` Direction Statement as an established system, completed specification, or validated standard.

## Preservation Rule

The following must be preserved:

- Original publication date
- Original version
- Author
- Document status
- Research status
- Canonical language
- Links to later versions or successor documents

When a later version is adopted, the earlier document remains in the repository.

## Formalization Sequence

The recommended sequence is:

1. Working Hypothesis
2. Direction Statement
3. Research Record
4. Direction Statement v1.0
5. Formal Definition
6. Concept Architecture
7. Editorial Principles
8. Formal Specification
9. Implementation and Case Records
10. Periodic Revision

Not every concept must pass through every stage, but no draft should be represented as a formal specification without an explicit formalization decision.
