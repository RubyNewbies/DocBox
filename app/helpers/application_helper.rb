module ApplicationHelper
  def sortable(column, title)
    title ||= column.titleize
    direction = column == sort_column && sort_direction == "asc" ? "desc" : "asc"
    link_to title, {:sort => column, :direction => direction}
  end

  def coderay(file)
    text = File.read(file.attachment.path)
    case file.extension
    when 'rb' then
      type = 'ruby'
    when 'py' then
      type = 'python'
    else
      type = file.extension
    end
    CodeRay.scan(text, type.to_sym).div
  end
end