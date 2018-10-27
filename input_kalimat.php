<?php

	if(isset($_POST['inputkalimat']))
	{
		$inputkalimat = $_POST['inputkalimat'];
		// print($inputkalimat);
		// print("<br>");
		if($inputkalimat != "")
		{
			shell_exec("python input_kalimat.py simpan_file \"$inputkalimat\"");
			echo '<script>alert("File telah tersimpan")</script>';
			shell_exec("python input_kalimat.py prediksi_pos");
			// shell_exec("python input_kalimat.py  pisah_kata_pos ");
			// shell_exec("python input_kalimat.py  prediksi_jeda ");
			// shell_exec("python input_kalimat.py  pisah_pos_jeda");
			// shell_exec("python input_kalimat.py  gabung_kata_jeda");

			
			//echo '<script>window.location="Utama.html"</script>';
		}


	}

?>