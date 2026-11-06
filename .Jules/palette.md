## 2024-05-24 - Screen Reader Support for Flashcard Updates
**Learning:** Dynamic text changes in single-page applications (like updating a flashcard letter) are not announced by screen readers by default.
**Action:** Always add `aria-live="polite"` and `aria-atomic="true"` to containers where text content changes dynamically without a page reload to ensure screen readers announce the new content.
