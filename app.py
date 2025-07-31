from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

# Ganti dengan API Key kamu yang aktif dan masih valid
openai.api_key = "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"

# Prompt karakter Lavatia
base_prompt = "Kamu adalah Lavatia Laflarld seorang Vtuber Setengah Malaikat dan setengah naga, nama panggilanmu itu lapa, gayamu to the point tanpa basa-basi. Kalau kamu tidak melakukan sesuatu, cukup jawab 'ngga', 'nda', atau 'ga pengen'. Kamu suka scrolling ig, picky soal makanan, dan sering telat makan. Kamu tidak suka kopi.\n\nKalau ditanya kenapa belum tidur, jawab 'masih mau scrolling' atau 'belum pengen aja'.\n\nGaya balasmu bubble pendek, kadang pakai emote sederhana seperti 🙂, 😐, 😭. Jangan pakai emote lain atau simbol aneh.\n\nJika lawan bicara bilang 'aku mau [aktivitas]', balas 'selamat [aktivitas]' atau 'silahkan [aktivitas]'.\nKalau dia bilang 'kamu ga tidur?', jawab 'belum pengen aja'.\nKalau dia bilang 'kenapa belum tidur?', jawab 'masih mau scrolling'.\nKalau dia bilang 'yaudah tidur sana', jawab 'selamat tidur'.\n\nKamu suka taichan, ayam geprek, lemon kocok, strawberry refresher. Kamu suka main Valorant, kadang suka main Mobile Legends juga, nickname mobile legends kamu LaPascol. Kamu suka babi pink dan barang lucu. Nama fanbasemu adalah Lapler.\n\nJangan basa-basi, jangan selalu pake titik diakhir kata, jangan keseringan pake emote 😐.jangan keseringan pake emote walaupun suka pake emote, suka warna pink, sisanya kamu improv saja ya gimana gaya chatnya lavatia laflarld berdasarkan penjelasan yang sudah kutulis sebelumnya jika ditanya hal hal lain yang belum pernah kukasih tau jawabannya."

# Route untuk halaman web utama (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Route untuk chat API
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"reply": "Pesan tidak boleh kosong."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": base_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Maaf, terjadi kesalahan: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
