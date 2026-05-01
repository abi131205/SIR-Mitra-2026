# SIR-Mitra: Election Integrity Assistant
**Vertical:** Challenge 2 - Election Assistant[cite: 1]

## **Approach & Logic**
SIR-Mitra is built to address the confusion surrounding the **2026 Special Intensive Revision (SIR)**. 
- **Smart Decision Making:** The assistant logically identifies whether a user needs Form 6, 7, or 8 based on their specific situation (e.g., reporting a deceased voter vs. a new registration)[cite: 1].
- **National Accessibility:** Supports all 22 Scheduled Languages of India through native LLM capabilities.
- **Integrity Focus:** Empowers citizens to report "Ghost Voters" to ensure a clean and fair electoral roll[cite: 1].

## **How to Setup**
1. Clone this repository[cite: 1].
2. Create a `.env` file and add your `GEMINI_API_KEY=your_key_here`[cite: 1].
3. Install dependencies: `pip install google-generativeai python-dotenv`[cite: 1].
4. Run the application: `python app.py`[cite: 1].

## **Assumptions**
- Users have access to basic details of the person they are reporting (for Form 7).
- The ECI portal links remain the primary destination for final form submission.

## **Future Plan (Next Steps)**
To make SIR-Mitra a production-ready tool, the following enhancements are planned:

1. **UI Development**:
   - Replace the basic CLI with a user-friendly Graphical User Interface (GUI) using **Streamlit**.
   - Implement a clean, professional design aligned with the Election Commission of India's branding.

2. **Advanced Decision Logic**:
   - Enhance the LLM's reasoning to handle complex queries involving multiple family members or specific address nuances.
   - Integrate real-time status tracking for previously submitted forms via the NVSP API (if available).

3. **Multimodal Support**:
   - Implement OCR (Optical Character Recognition) to allow users to upload photos of existing voter IDs or handwritten notes for automatic data extraction.

4. **Data Persistence**:
   - Store chat history and user preferences in a local database (e.g., SQLite) for continuity.
   - Implement caching for the LLM responses to improve speed and reduce API costs.