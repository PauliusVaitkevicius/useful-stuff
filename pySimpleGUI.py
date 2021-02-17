import PySimpleGUI as sg

window = sg.Window(
    "Title",
    icon=PATH_ICON,
    no_titlebar=False,
    background_color=color_background,
    font=font_main,
    element_justification="left",
    use_default_focus=False,
    keep_on_top=False,
).Layout(layout)
window.Finalize()

while True:
    error_message = "KLAIDA:\n"
    error_message_initial = error_message
    event, values = window.Read()

    # print(event)

    if not values["FOLDER"]:
        error_message += "  - Nenurodytas katalogas.\n"

    vd_type = list(values.keys())[list(values.values()).index(True)]
    vd_folder = values["FOLDER"]

    if event in (None, "Tvarkyti vykdomuosius dokumentus"):
        if len(error_message) > len(error_message_initial):
            display_error_message_box(title="Klaida", message=error_message)
            print(error_message)
        else:
        # all actiong goes here

        # updatin progress bar example
        window.Element("VD_OCR_PROGR_TXT").Update(
            "{}% | {} iš {}".format(0, 0, files_count)
        )
        window.Element("VD_TV_PROGR_TXT").Update(
            "{}% | {} iš {}".format(0, 0, files_count)
        )
        window.Element("VD_STATUS_LINE_TXT").Update(
            "vyksta dokumentų atpažinimas"
        )

        #         another example

        for idx, pdf_file_name in enumerate(files_content_todo, start=1):
            prog_proc = prog_bar_max * idx // files_count

            window.Element("VD_TV_PROGR_BAR").Update(
                prog_proc, prog_bar_max, visible=True
            )
            window.Element("VD_TV_PROGR_TXT").Update(
                "{}% | {} iš {}".format(prog_proc, idx, files_count),
                visible=True,
            )

            # print(files_content_todo[idx - 1][0])

            window.Element("VD_STATUS_LINE_TXT").Update(
                "tvarkomas {}".format(files_content_todo[idx - 1][0])
            )
            window.Refresh()


# --- in separate layout.py file:


prog_bar_max = 100

message = (
    "Jūs paleidote vykdomųjų dokumentų (VD) tvarkymo robotą. \n"
    "Jums reikės pasirinkti tvarkomų VD katalogą ir tvarkomų VD tipą."
)

layout = [
    [
        sg.Image(
            resource_path(
                PATH_PROGRAM + get_config_value("img", "logo")),
            background_color=color_background,
            pad=element_pad,
        ),
        sg.Text(
            "X",
            size=(40, 2),
            justification="center",
            font='"Cambria" 18 bold',
            background_color=color_background,
            text_color=color_button_browse,
            pad=element_pad,
        ),
    ],
    [
        sg.Text(
            message,
            background_color=color_background,
            text_color=color_text,
            pad=element_pad,
        )
    ],
    [
        sg.Text(
            "X",
            size=(30, 1),
            background_color=color_background,
            text_color=color_text,
        ),
        sg.InputText("", key="FOLDER"),
        sg.FolderBrowse(
            button_text="Ieškoti katalogo",
            button_color=("white", color_button_browse),
        ),
    ],
    # ---------- RADIO ---------------------------------------------------------------------------------
    [
        sg.T(
            "A",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        )
    ],
    [
        sg.T(
            "\t",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        ),
        sg.Radio(
            "B",
            group_id="RADIO2",
            default=True,
            background_color=color_background,
            key="VD_NOTARAI",
            text_color=color_text,
            auto_size_text=True,
            disabled=False,
        ),
    ],
    [
        sg.T(
            "\t",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        ),
        sg.Radio(
            "C",
            group_id="RADIO2",
            default=False,
            background_color=color_background,
            key="VD_TEISMAI",
            text_color=color_text,
            auto_size_text=True,
            disabled=True,
        ),
    ],
    [
        sg.T(
            "\t",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        ),
        sg.Radio(
            "D",
            group_id="RADIO2",
            default=False,
            background_color=color_background,
            key="VD_VMI",
            text_color=color_text,
            auto_size_text=True,
            disabled=True,
        ),
    ],
    [
        sg.T(
            "\t",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        ),
        sg.Radio(
            "E",
            group_id="RADIO2",
            default=False,
            background_color=color_background,
            key="VD_SODRA",
            text_color=color_text,
            auto_size_text=True,
            disabled=True,
        ),
    ],
    [
        sg.T(
            "\t",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        ),
        sg.Radio(
            "F",
            group_id="RADIO2",
            default=False,
            background_color=color_background,
            key="VD_POLICIJA",
            text_color=color_text,
            auto_size_text=True,
            disabled=True,
        ),
    ],

    # ---------- PROGRESS BAR -----------------------------------------------------------------------------
    [
        sg.T(
            "X:",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        )
    ],
    [
        sg.ProgressBar(
            max_value=prog_bar_max,
            orientation="horizontal",
            size=(50, 20),
            metadata="Test",
            key="OCR_PROGR_BAR",
        ),
        sg.Text(
            "",
            size=(15, 1),
            background_color=color_background,
            text_color=color_text,
            justification="center",
            key="OCR_PROGR_TXT",
        ),
    ],
    # ---------- PROGRESS BAR -----------------------------------------------------------------------------
    [
        sg.T(
            "Y",
            background_color=color_background,
            text_color=color_text,
            justification="left",
        )
    ],
    [
        sg.ProgressBar(
            max_value=prog_bar_max,
            orientation="horizontal",
            size=(50, 20),
            metadata="Test",
            key="TV_PROGR_BAR",
        ),
        sg.Text(
            "",
            size=(15, 1),
            background_color=color_background,
            text_color=color_text,
            justification="center",
            key="TV_PROGR_TXT",
        ),
    ],
    # ---------- STATUS TEXT LINE -----------------------------------------------------------------------------
    [
        sg.Text(
            "Z: ",
            # size=(10, 1),
            background_color=color_background,
            text_color=color_status_text,
            justification="left",
        ),
        sg.Text(
            "",
            size=(60, 1),
            font="Cambria 12 italic",
            background_color=color_background,
            text_color=color_status_text,
            justification="left",
            key="STATUS_LINE_TXT",
        ),
    ],
]
