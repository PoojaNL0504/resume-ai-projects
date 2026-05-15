const BASE_URL = "http://127.0.0.1:8000";

let isProcessing = false;
window.awaitingJD = false;

/* ------------------ CHAT MESSAGE ------------------ */
function addMessage(text, type) {
    const chatBox = document.getElementById("chatBox");

    const div = document.createElement("div");
    div.className = type;
    div.innerText = text;

    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

/* ------------------ UPLOAD RESUME ------------------ */
async function uploadResume() {
    const file = document.getElementById("resumeFile").files[0];

    if (!file) {
        addMessage("⚠️ Please select a resume file first.", "bot");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const res = await fetch(`${BASE_URL}/upload_resume`, {
            method: "POST",
            body: formData
        });

        await res.json();

        addMessage("✅ Resume uploaded successfully!", "bot");
        showATSButton();

    } catch (err) {
        addMessage("⚠️ Upload failed. Try again.", "bot");
    }
}

/* ------------------ ASK QUESTION ------------------ */
async function askQuestion(question) {
    try {
        const res = await fetch(`${BASE_URL}/chat`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question })
        });

        const data = await res.json();
        addMessage(data.answer, "bot");

    } catch {
        addMessage("⚠️ Chat failed. Try again.", "bot");
    }
}

/* ------------------ SHOW ATS BUTTON ------------------ */
function showATSButton() {
    const chatBox = document.getElementById("chatBox");

    const div = document.createElement("div");
    div.className = "bot";

    div.innerHTML = `
        <p>What would you like to do next?</p>
        <button class="action-btn" onclick="checkATS()">
            <i data-lucide="bar-chart-3"></i>
            Check ATS Score
        </button>
    `;

    chatBox.appendChild(div);
    lucide.createIcons(); 
}

/* ------------------ TRIGGER ATS ------------------ */
function checkATS() {
    addMessage("📄 Paste the Job Description to check ATS score.", "bot");
    window.awaitingJD = true;
}

/* ------------------ HANDLE USER INPUT ------------------ */
async function handleUserInput() {
    if (isProcessing) return;
    isProcessing = true;

    const inputEl = document.getElementById("question");
    const input = inputEl.value.trim();

    if (!input) {
        isProcessing = false;
        return;
    }

    addMessage(input, "user");
    inputEl.value = "";

    try {
        // 🔥 ATS FLOW
        if (window.awaitingJD) {
            window.awaitingJD = false;

            addMessage("⏳ Analyzing ATS score...", "bot");

            const res = await fetch(`${BASE_URL}/check_ats`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ jd: input })
            });

            const data = await res.json();

            let message = ` ATS Score: ${data.ats_score}%\n\n`;

            message += " Missing Skills:\n";
            data.missing_skills.forEach(s => message += `• ${s}\n`);

            message += "\n Improvements:\n";
            data.improvements.forEach(i => message += `• ${i}\n`);

            addMessage(message, "bot");

        } else {
            await askQuestion(input);
        }

    } catch {
        addMessage("⚠️ Something went wrong. Try again.", "bot");
    }

    isProcessing = false;
}

/* ------------------ ENTER KEY FIX ------------------ */
document.getElementById("question").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        e.preventDefault(); 
        handleUserInput();
    }
});
function toggleTheme() {
    const body = document.body;
    const btn = document.getElementById("themeToggle");

    body.classList.toggle("light");

    if (body.classList.contains("light")) {
        btn.innerHTML = '<i data-lucide="sun"></i>';
        localStorage.setItem("theme", "light");
    } else {
        btn.innerHTML = '<i data-lucide="moon"></i>';
        localStorage.setItem("theme", "dark");
    }

    lucide.createIcons(); 
}

window.onload = () => {
    const saved = localStorage.getItem("theme");
    const btn = document.getElementById("themeToggle");

    if (saved === "light") {
        document.body.classList.add("light");
        btn.innerHTML = '<i data-lucide="sun"></i>';
    } else {
        btn.innerHTML = '<i data-lucide="moon"></i>';
    }

    lucide.createIcons();
};

document.getElementById("resumeFile").addEventListener("change", function() {
    const fileName = this.files[0]?.name || "📄 Choose Resume";
    document.querySelector(".file-upload span").innerText = fileName;
});