const SMALL_HEIGHT = 100;
const LARGE_HEIGHT = 500;


function resize_codemirror(codeMirrorElement, expandButton, shortenButton, expand=true) {
    if (expand) {
        codeMirrorElement.setSize(null, LARGE_HEIGHT)
        expandButton.hide()
        shortenButton.show()
    } else {
        codeMirrorElement.setSize(null, SMALL_HEIGHT)
        shortenButton.hide()
        expandButton.show()
    }
}


function set_resize_buttons(codeRunner, expandEditorId, shortenEditorId, expandConsoleId, shortenConsoleId) {
    let expandEditorButton = get_code_block_element(expandEditorId)
    let shortenEditorButton = get_code_block_element(shortenEditorId)
    let expandConsoleButton = get_code_block_element(expandConsoleId)
    let shortenConsoleButton = get_code_block_element(shortenConsoleId)

    resize_codemirror(codeRunner.codeEditor, expandEditorButton, shortenEditorButton, false)
    resize_codemirror(codeRunner.terminalEditor, expandConsoleButton, shortenConsoleButton, false)
    shortenEditorButton.hide()
    shortenConsoleButton.hide()

    expandEditorButton.on("click", () => {
        resize_codemirror(codeRunner.codeEditor, expandEditorButton, shortenEditorButton, true)
    })
    shortenEditorButton.on("click", () => {
        resize_codemirror(codeRunner.codeEditor, expandEditorButton, shortenEditorButton, false)
    })
    expandConsoleButton.on("click", () => {
        resize_codemirror(codeRunner.terminalEditor, expandConsoleButton, shortenConsoleButton, true)
    })
    shortenConsoleButton.on("click", () => {
        resize_codemirror(codeRunner.terminalEditor, expandConsoleButton, shortenConsoleButton, false)
    })
}
