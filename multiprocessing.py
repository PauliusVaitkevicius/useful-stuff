import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm

num_cores = multiprocessing.cpu_count()

count = 0

with tqdm(total=vd_files_count) as pbar:
    # let's give it some more threads:
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = {
            executor.submit(read_file_in_parallel, arg): arg for arg in vd_files_todo
        }
        for future in concurrent.futures.as_completed(futures):
            count += 1

            (pdf_file_name, pdf_file_path, pdf_file_text) = future.result()

            vd_files_content_todo = np.append(
                vd_files_content_todo,
                [[pdf_file_name, pdf_file_path, pdf_file_text]],
                axis=0,
            )

            pbar.update(1)

            prog_proc = prog_bar_max * count // vd_files_count

            window.Element("VD_OCR_PROGR_BAR").Update(
                prog_proc, prog_bar_max, visible=True
            )
            window.Element("VD_OCR_PROGR_TXT").Update(
                "{}% | {} iš {}".format(prog_proc, count, vd_files_count),
                visible=True,
            )
            window.Refresh()
