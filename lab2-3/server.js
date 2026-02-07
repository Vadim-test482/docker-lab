import express from "express";
const app = express();

app.get("/", (req, res) => res.json({ ok: true, msg: "Express in Docker" }));
app.listen(3000, "0.0.0.0", () => console.log("Listening on 3000"));
