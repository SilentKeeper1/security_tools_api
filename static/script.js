async function generatePassword(){
    const res = await fetch('/password');
    const data = await res.json();
    document.getElementById('passwordResult').innerText = data.password;
}


async function geoipLookup(){
    const ip = document.getElementById('geoipInput').value;
    const res = await fetch(`/geoip?ip=${ip}`);
    const data = await res.json();
    document.getElementById('geoipResult').innerText = JSON.stringify(data, null, 2);
}

async function checkStrength() {
    const pw = document.getElementById('pwInput').value;
    const res = await fetch('/password_strength', {
       method: 'POST',
       headers: { 'Content-Type': 'application/json' },
       body: JSON.stringify({ password: pw })
     });
     const data = await res.json();
     document.getElementById('pwStrengthResult').innerText = `Strength: ${data.strength}`;
     
}