const tellIssueBtn = document.getElementById('tellIssue');
const modal = document.getElementById('modal');
const modalMessage = document.getElementById('modalMessage');
const modalVerify = document.getElementById('modalVerify');
const modalCancel = document.getElementById('modalCancel');
const verifyBtn = document.getElementById('verify');
const queryBox = document.getElementById('query');
const outputDiv = document.getElementById('output');
const exportBtn = document.getElementById('export');
const clearBtn = document.getElementById('clear');
const themeToggleBtn = document.getElementById('themeToggle');

let timerInterval;
let remainingSeconds = 20;

// Configure recording duration (seconds)
const RECORD_DURATION = 20;

// Set fixed width for Tell the Issue button via CSS
// (removed inline style from HTML)
tellIssueBtn.style.width = '250px';
tellIssueBtn.style.flex = 'none';

function showModal(message, showVerify=false, showCancel=false){
    modalMessage.textContent = message;
    modalVerify.style.display = showVerify ? 'inline-block' : 'none';
    modalCancel.style.display = showCancel ? 'inline-block' : 'none';
    modal.style.display = 'flex';
}

function hideModal(){
    modal.style.display = 'none';
}

// Override existing startTimer to use RECORD_DURATION
function startTimer(){
    remainingSeconds = RECORD_DURATION;
    showModal(`Recording: ${remainingSeconds}s remaining`);
    timerInterval = setInterval(()=>{
        remainingSeconds--;
        if(remainingSeconds>0){
            modalMessage.textContent = `Recording: ${remainingSeconds}s remaining`;
        } else {
            clearInterval(timerInterval);
            // Timer finished, but transcription will be handled after recording
        }
    },1000);
}

// Global variable to hold temp file after recording
let tempFileGlobal = null;

// Async function to start recording and store temp file
async function startRecording(){
    try {
        const res = await fetch(`/record_audio?duration=${RECORD_DURATION}`);
        const data = await res.json();
        if(!res.ok){
            throw new Error(data.error || 'Recording failed');
        }
        tempFileGlobal = data.temp_file;
        console.log('Recording finished', tempFileGlobal);
        // After recording finishes, start transcription
        transcribeAfterTimer();
    } catch(err){
        console.error(err);
        hideModal();
        outputDiv.innerHTML = `<p>Recording error: ${err.message||'Please try again.'}</p>`;
    }
}

// Transcribe after timer ends
async function transcribeAfterTimer(){
    showModal('Transcribing audio...');
    try {
        const transRes = await fetch('/transcribe', {
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({file:tempFileGlobal})
        });
        const transData = await transRes.json();
        if(!transRes.ok){
            throw new Error(transData.error||'Transcription failed');
        }
        const transcript = transData.text || '';
        // Show transcription modal with textarea
        showTranscriptionModal(transcript);
    } catch(err){
        console.error(err);
        hideModal();
        outputDiv.innerHTML = `<p>Transcription error: ${err.message||'Please try again.'}</p>`;
    }
}

// Function to show transcription modal with textarea and Proceed/Cancel
function showTranscriptionModal(initialText){
    modalMessage.innerHTML = '';
    const textarea = document.createElement('textarea');
    textarea.id = 'transcriptText';
    textarea.style.width = '100%';
    textarea.style.height = '200px';
    textarea.value = initialText;
    modalMessage.appendChild(textarea);
    const btnContainer = document.createElement('div');
    btnContainer.style.marginTop='10px';
    const proceedBtn = document.createElement('button');
    proceedBtn.textContent='Proceed';
    proceedBtn.style.marginRight='10px';
    proceedBtn.style.padding='5px 10px';
    const cancelBtn = document.createElement('button');
    cancelBtn.textContent='Cancel';
    cancelBtn.style.padding='5px 10px';
    btnContainer.appendChild(proceedBtn);
    btnContainer.appendChild(cancelBtn);
    modalMessage.appendChild(btnContainer);
    modal.style.display='flex';
    // Hide verify/cancel buttons
    modalVerify.style.display='none';
    modalCancel.style.display='none';
    // Proceed action
    proceedBtn.onclick = async () => {
        hideModal();
        const text = textarea.value;
        outputDiv.innerHTML = '<p>Analyzing your legal query...</p>';
        try {
            const response = await fetch('/process', {
                method:'POST',
                headers:{'Content-Type':'application/json'},
                body:JSON.stringify({text})
            });
            const data = await response.json();
            if(!response.ok){
                throw new Error(data.error||'Request failed');
            }
            const markdown = parseServerResponse(data);
            renderMarkdown(markdown);
        } catch(err){
            console.error(err);
            outputDiv.innerHTML = `<p>Unable to process the request.</p><p>${err.message||'Please try again.'}</p>`;
        }
    };
    cancelBtn.onclick = () => { hideModal(); };
}

// Attach click event to button
tellIssueBtn.addEventListener('click', () => {
    startTimer();
    startRecording();
});

function setTheme(theme) {
    const isDark = theme === 'dark';
    document.body.classList.toggle('theme-dark', isDark);
    document.body.classList.toggle('theme-light', !isDark);
    themeToggleBtn.textContent = isDark ? '☀️ Light' : '🌙 Dark';
}

themeToggleBtn.addEventListener('click', () => {
    const isDark = document.body.classList.contains('theme-dark');
    setTheme(isDark ? 'light' : 'dark');
});

function renderMarkdown(md) {
    if (!md) {
        outputDiv.innerHTML = '<p>Ready for your legal query.</p>';
        return;
    }

    const parsed = typeof marked !== 'undefined' ? marked.parse(md) : md;
    const safeHtml = typeof DOMPurify !== 'undefined' ? DOMPurify.sanitize(parsed) : parsed;
    outputDiv.innerHTML = safeHtml;

    // Remove table header rows that contain "Item" and "Value"
    const tables = outputDiv.querySelectorAll('table');
    tables.forEach(t => {
        const header = t.querySelector('tr');
        if (header && header.querySelectorAll('th').length > 0) {
            header.remove();
        }
    });
}

function parseServerResponse(data) {
    if (!data) return '';
    if (typeof data === 'string') return data;
    if (data.error) throw new Error(data.error);
    if (data.markdown) return data.markdown;
    if (data.result) return data.result;
    return JSON.stringify(data, null, 2);
}

exportBtn.addEventListener('click', () => {
    const html = `
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Legal Compass Export</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 32px; background: #f5f8ff; color: #0f2740; }
        .box { background: white; border-radius: 18px; padding: 24px; box-shadow: 0 10px 30px rgba(0,0,0,0.08); }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #dfe9f5; padding: 8px 12px; text-align: left; }
        code { background: #edf3ff; padding: 2px 6px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="box">${outputDiv.innerHTML}</div>
</body>
</html>`;

    const blob = new Blob([html], { type: 'text/html' });
    const a = document.createElement('a');
    const ts = new Date().toISOString().replace(/[:.]/g, '-');
    a.href = URL.createObjectURL(blob);
    a.download = `legal-compass-output-${ts}.html`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(a.href);
});

clearBtn.addEventListener('click', () => {
    outputDiv.innerHTML = '<p>Output cleared.</p>';
    queryBox.value = '';
    queryBox.focus();
});

setTheme('light');
renderMarkdown('## Legal Compass\n\nThis is where your legal analysis results will appear.');