out_path <- file.path(Sys.getenv("OUTPUT_DIR", unset = "."), "plot.png")
png(filename = out_path)
plot(1:10, col = "blue", main = "Static R Plot", xlab = "X Axis", ylab = "Y Axis")
dev.off()
cat("✅ plot.png saved to:", out_path, "\n")

png(file.path(Sys.getenv("OUTPUT_DIR", unset = "."), "plot.png"))
plot(1:10, main = "Test Plot")
dev.off()
