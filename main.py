import functions_metal as fm
import upload_data

fm.search_with_text("Generals gathered in their masses", [{
        "field": "formed",
        "value": 1984
    }])

fm.search_with_text("Generals gathered in their masses", [{
        "field": "genre",
        "value": "Heavy Metal"
    }])

fm.search_with_text("Generals gathered in their masses", [{
        "field": "origin",
        "value": "London, England"
    }])

fm.delete_with_payload("101")

