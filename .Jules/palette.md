## 2024-11-04 - Dynamic Content Accessibility
**Learning:** Screen readers won't automatically announce when JS changes the content of an element (like a flashcard changing letters), leaving non-visual users unaware of the change.
**Action:** Use `aria-live="polite"` (or `"assertive"`) on containers whose content updates dynamically without a page reload so screen readers announce the changes.
