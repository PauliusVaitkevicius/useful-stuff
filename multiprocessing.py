import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from tqdm import tqdm
import numpy as np

num_cores = multiprocessing.cpu_count()

count = 0

with tqdm(total=vd_files_count) as pbar:
    # let's give it some more threads:
    # with concurrent.futures.ThreadPoolExecutor() as executor:
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = {
            executor.submit(call_function, arg): arg for arg in argument_array
        }
        for future in concurrent.futures.as_completed(futures):
            count += 1

            (x,y,z) = future.result()

            save_results_ndarray = np.append(
                save_results_ndarray,
                [[x,y,z]],
                axis=0,
            )

            pbar.update(1)

            # update progress bar on pySimpleGUI window

            prog_proc = prog_bar_max * count // total

            window.Element("VD_OCR_PROGR_BAR").Update(
                prog_proc, prog_bar_max, visible=True
            )
            window.Element("VD_OCR_PROGR_TXT").Update(
                "{}% | {} iš {}".format(prog_proc, count, vd_files_count),
                visible=True,
            )
            window.Refresh()
