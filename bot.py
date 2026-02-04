import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from back import Dispatcher

load_dotenv('.env')

BOT_TOKEN = os.getenv("telegram_key")
def build_plot(data: dict, output_file="plot.png"):
    coords = list(data.keys())
    clouds = [v['cloud_height'] for v in data.values()] 

    x = range(len(coords))
    y = clouds

    plt.figure()
    plt.scatter(x, y, s=50)
    plt.plot(x, y)

    labels = [f"{lat:.4f},{lon:.4f}" for lat, lon in coords]
    plt.xticks(x, labels, rotation=45, ha="right")

    plt.ylabel("Cloud height")
    plt.xlabel("Points")

    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    return output_file

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Пришли KML файл.")

async def handle_kml(update: Update, context: ContextTypes.DEFAULT_TYPE):
    document = update.message.document

    if not document.file_name.endswith(".kml"):
        await update.message.reply_text("Нужен .kml файл")
        return

    file = await document.get_file()
    kml_path = "input.kml"

    await file.download_to_drive(kml_path)

    await update.message.reply_text("Считаю облака...")

    disp = Dispatcher()
    kml_dict = disp.create_parce_kml(kml_path)
    result_dict = disp.from_epsi(kml_dict)

    plot_file = build_plot(result_dict)


    await update.message.reply_photo(photo=open(plot_file, "rb"))

    os.remove(kml_path)
    os.remove(plot_file)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.ALL, handle_kml))

app.run_polling()
