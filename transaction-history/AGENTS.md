# AI Contribution Guidelines

## Scope

- Make changes for the transaction history project inside this folder unless a repository-level change is required.
- Use the GitHub `Transaction_History` project and its issues as the source of truth for planned work.
- Keep each change focused on one issue or clearly related feature.

## Implementation

- Inspect the existing code and tests before editing.
- Prefer simple, readable implementations that match the project's existing style.
- Preserve existing behavior unless the issue explicitly requires a change.
- Do not add dependencies unless they are necessary and documented.

## Transaction Data

- Treat transaction data as potentially sensitive.
- Do not commit credentials, API keys, personal data, or real financial records.
- Use representative mock data in tests and examples.
- Validate user-provided search, date, and category values at the application boundary.

## Testing

- Add or update focused tests for every behavior change.
- Cover normal cases, empty results, invalid input, and relevant boundary conditions.
- Run the project's available tests before committing.

## Git Workflow

- Name feature branches using `issue-number/feature/title`, for example `2/feature/add-category-filtering` for issue #2.
- Keep commits small and describe the behavior they add or change.
- Reference the related GitHub issue when appropriate.
- Review the diff before pushing and avoid unrelated formatting or generated files.
