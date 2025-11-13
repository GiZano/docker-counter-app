async function incrementCounter(name) {
    const response = await fetch('/increment/' + name);
    const data = await response.json();
    document.getElementById(name + '-value').textContent = data.value;
}

async function resetCounter(name) {
    await fetch('/reset/' + name);
    document.getElementById(name + '-value').textContent = '0';
}

// Carica i valori iniziali
async function loadCounters() {
    const counters = ['visits', 'clicks'];
    for (const counter of counters) {
        const response = await fetch('/get/' + counter);
        const data = await response.json();
        document.getElementById(counter + '-value').textContent = data.value;
    }
}

document.addEventListener('DOMContentLoaded', loadCounters());