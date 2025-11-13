## Interactive

### Disclosure

Disclosure is an optionally controlled component used to put long sections of information under content blocks that users can expand or collapse by pressing an activator.

**Props:**

*   `defaultOpen`: `MaybeResponsiveConditionalStyle<DisclosureOpen | undefined>` - For uncontrolled disclosure components, the default `open` state on the initial render.
*   `onToggle`: `(open: string[]) => void` - Callback fired when the open state of the disclosure changes.
*   `open`: `DisclosureOpen` - For controlled disclosure components, the open state.
*   `transition`: `"none"` - Set to `'none'` to disable the default transition animation.