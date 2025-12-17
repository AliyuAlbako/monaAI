import { useState } from "react";
import { sendMessage } from "../services/api";
import Message from "./Message";
import ChatInput from "./ChatInput";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSend = async (text) => {
    setMessages((prev) => [...prev, { text, sender: "user" }]);
    setLoading(true);

    try {
      const data = await sendMessage(text, sessionId);

      if (!sessionId && data.session_id) {
        setSessionId(data.session_id);
      }

      setMessages((prev) => [
  ...prev,
  {
    text: data.response,
    sender: "assistant",
    language: data.language,
  },
]);

    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { text: "Server error. Try again.", sender: "assistant" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "600px",
        margin: "40px auto",
        border: "1px solid #ddd",
        padding: "15px",
        display: "flex",
        flexDirection: "column",
        height: "80vh",
      }}
    >
      <div style={{ flex: 1, overflowY: "auto", marginBottom: "10px" }}>
        {messages.map((msg, idx) => (
          <Message key={idx} text={msg.text} sender={msg.sender} />
        ))}
        {loading && <Message text="Typing..." sender="assistant" />}
      </div>

      <ChatInput onSend={handleSend} />
    </div>
  );
}
