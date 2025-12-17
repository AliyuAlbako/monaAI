export default function Message({ text, sender, language }) {
  return (
    <div
      style={{
        maxWidth: "70%",
        marginBottom: "10px",
        alignSelf: sender === "user" ? "flex-end" : "flex-start",
        background: sender === "user" ? "#DCF8C6" : "#F1F1F1",
        padding: "10px 14px",
        borderRadius: "10px",
      }}
    >
      {language && (
        <small style={{ fontSize: "10px", opacity: 0.6 }}>
          {language.toUpperCase()}
        </small>
      )}
      <div>{text}</div>
    </div>
  );
}
