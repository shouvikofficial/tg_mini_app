const tg = window.Telegram.WebApp;
tg.expand(); // Expands the mini app

function submitAddress() {
    const address = document.getElementById("address").value;
    if (!address.trim()) {
        alert("Please enter an address.");
        return;
    }

    fetch("https://your-backend-url.com/submit", {  // Replace with your actual backend URL
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            user_id: tg.initDataUnsafe?.user?.id || "unknown",
            address: address
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        tg.close();
    })
    .catch(error => console.error("Error:", error));
}
