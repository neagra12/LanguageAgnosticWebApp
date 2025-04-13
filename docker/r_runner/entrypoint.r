# entrypoint.R

args <- commandArgs(trailingOnly = TRUE)

# 🛑 Validate arguments
if (length(args) == 0 || args[1] == "") {
  stop("❌ No script path provided to entrypoint.R.")
}

script_path <- args[1]

cat("📄 Running R script at:", script_path, "\n")

# ✅ Source the script
source(script_path)

cat("✅ R script executed successfully.\n")


