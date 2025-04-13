library(fs)

cat("📁 Scanning for script.R in subfolders...\n")

script_files <- dir_ls(path = "/app/outputs", recurse = TRUE, glob = "*/script.R")

for (script_path in script_files) {
  cat("📄 Found script:", script_path, "\n")

  # Set OUTPUT_DIR before sourcing
  output_dir <- dirname(script_path)
  Sys.setenv(OUTPUT_DIR = output_dir)

  tryCatch({
    source(script_path)
    cat("✅ Script executed successfully.\n")
  }, error = function(e) {
    cat("❌ Error running script:", e$message, "\n")
  })
}
