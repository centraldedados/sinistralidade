require 'httparty'
require 'nokogiri'
require 'fileutils'

pdf_directory = "pdfs"
sleep_time = 30
url_relatorios = "http://www.ansr.pt/Estatisticas/RelatoriosDeSinistralidade/Pages/default.aspx"

puts "Requesting reports..."
page_relatorios = HTTParty.get(url_relatorios, { headers: {"User-Agent" => "Firefox"}})

puts "Parsing reports links..."
page = Nokogiri::HTML(page_relatorios.parsed_response.to_s)


document_links = page.css('.subareaItem a').map { |link| link['href'] }

document_links_size = document_links.length

document_links.each_with_index do |d, index|
  puts
  puts "#{index+1}/#{document_links_size}: #{d}"
  filename = d.split('/').last
  year_directory = d.split('/')[6]
  FileUtils.mkdir_p "#{pdf_directory}/#{year_directory}" # create year directory if it doesn't exist
  filename_path = File.join(pdf_directory, year_directory, filename) # path to file + filename
  if File.file?(filename_path)
    puts "File already saved, moving on to the next.."
  else
    puts "Requesting report..."
    report = HTTParty.get(URI.escape(d), { headers: {"User-Agent" => "Internet Explorer"}})
    puts "Saving PDF file..."
    open(filename_path, "wb") do |file|
      file.write(report.parsed_response)
    end
    #puts "Sleeping #{sleep_time} seconds..."
    #sleep sleep_time
  end
end



