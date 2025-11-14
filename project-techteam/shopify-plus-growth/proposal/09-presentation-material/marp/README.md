# Marp Presentation - HBNO Growth Accelerator

This folder contains the Marp markdown presentation for the HBNO Growth Accelerator proposal.

## What is Marp?

Marp (Markdown Presentation Ecosystem) allows you to create beautiful slide decks using Markdown syntax.

## Prerequisites

Install Marp CLI:

```bash
npm install -g @marp-team/marp-cli
```

Or use the VS Code extension:
- Install "Marp for VS Code" extension from the marketplace

## Files

- `presentation.md` - Main presentation file with embedded styling
- `README.md` - This file

## How to Use

### Option 1: VS Code Extension (Recommended)

1. Install "Marp for VS Code" extension
2. Open `presentation.md`
3. Click the preview button in the top right corner
4. Export to PDF/HTML/PPTX using the command palette (Cmd+Shift+P)

### Option 2: Command Line

Generate HTML:
```bash
marp presentation.md -o presentation.html
```

Generate PDF:
```bash
marp presentation.md -o presentation.pdf --pdf
```

Generate PowerPoint:
```bash
marp presentation.md -o presentation.pptx
```

With custom theme and options:
```bash
marp presentation.md -o presentation.html --html --allow-local-files
```

### Option 3: Watch Mode (for live editing)

```bash
marp -w presentation.md
```

## Presentation Features

- **15 slides** covering the complete proposal
- **Custom styling** embedded in the markdown
- **Color-coded metrics** (green for positive, red for negative)
- **Responsive tables** for data comparison
- **Split-screen layouts** for side-by-side comparisons
- **Callout boxes** for important information
- **Consistent branding** throughout

## Customization

All styling is embedded in the frontmatter of `presentation.md`. To customize:

1. Edit the `style:` section in the frontmatter
2. Modify colors, fonts, spacing as needed
3. Preview changes in real-time with watch mode

## Color Palette

- **Primary Blue:** #1E3A8A (headings, brand color)
- **Success Green:** #059669 (positive metrics)
- **Danger Red:** #DC2626 (negative metrics)
- **Warning Orange:** #F59E0B (caution/emphasis)
- **Neutral Gray:** #1F2937 (body text)

## Tips

- Use the preview mode to see slides as you edit
- Each `---` creates a new slide
- HTML is supported for advanced layouts
- Emojis work great for visual impact
- Tables are automatically styled

## Exporting

For best results when exporting:
- **PDF:** Best for sharing and printing
- **HTML:** Best for web presentation
- **PPTX:** Best for editing in PowerPoint

## Presenting

To present:
1. Export to HTML
2. Open in Chrome/Firefox
3. Press `F` for fullscreen
4. Use arrow keys to navigate

Or:
1. Export to PDF
2. Present using any PDF viewer
3. Use presentation mode for clean display

## Support

For Marp documentation: https://marp.app/
For VS Code extension: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode
